#!/usr/bin/env python3
"""
Elastic Security Advisories (GitHub repository files) - API Connectivity & Flow Test
====================================================================================

Exercises the exact GitHub REST API flow proposed for the `elastic_security_advisories`
CEL integration: enumerate every advisory file under a directory in a (private) GitHub
repository with the Git Trees API, revalidate that listing with a conditional request to
prove the zero-cost polling property, then fetch file contents with the Git Blobs API.

Because the source repository `elastic/security-advisories` is private and its on-disk
advisory format could not be observed during research, this script also reports what it
finds: file extensions, detected content format (JSON / YAML / YAML front matter +
Markdown / Markdown / other), and a decoded preview of each file. That output is the
single most valuable thing to send back, because it closes the largest open question in
the research brief.

Vendor-side setup
-----------------
You need a GitHub Personal Access Token that can read the repository's contents. Use a
fine-grained token; the classic `repo` scope also works but grants read/write across every
repository you can see.

 1. Sign in to GitHub as a user who already has read access to the repository.
    If you cannot browse https://github.com/elastic/security-advisories in a browser while
    signed in, stop here and request repository access first. No token can grant you access
    you do not already have.

 2. Go to: Settings -> Developer settings -> Personal access tokens -> Fine-grained tokens
    Direct link: https://github.com/settings/personal-access-tokens/new

 3. Set "Resource owner" to the ORGANIZATION that owns the repository (for example
    `elastic`), NOT your own user account.

    This is the single most common mistake. The selector defaults to your personal account.
    A user-owned token authenticates successfully, reports a healthy 5,000/hour rate limit,
    and then returns HTTP 404 for the organization's private repository with no explanation
    of why.

 4. Set "Repository access" to "Only select repositories" and choose the advisories
    repository.

 5. Under "Repository permissions", set:
        Contents  ->  Read-only        (required; this is the only permission needed)
        Metadata  ->  Read-only        (mandatory on every fine-grained token, granted
                                        automatically - there is nothing to enable)

 6. Set an expiration. Organizations commonly cap fine-grained token lifetime at 366 days.
    A token that violates the organization's maximum-lifetime policy is not rejected at
    creation - it is silently rejected at use time, again with a 404.

 7. Generate the token and copy it. It is shown only once.

 8. WAIT FOR APPROVAL. For organization-owned resources, fine-grained tokens require
    approval by an organization owner by default. Until approved, the token sits in a
    `pending` state and can read only public resources. Organization owners are notified
    by a once-daily digest email, so this step can take a day. You can check the token's
    status on the fine-grained tokens page.

 9. SAML SSO. If the organization enforces SAML single sign-on (the `elastic` organization
    does), note that fine-grained tokens are authorized during token creation, so there is
    no extra step. If you instead use a CLASSIC token, you MUST additionally click
    "Configure SSO" -> "Authorize" next to the token, or every request will return 404.

Diagnosing failures
-------------------
GitHub returns HTTP 404 - not 403 - for a private resource a credential cannot see. As a
result, four completely different faults produce a byte-identical `{"message":"Not Found"}`:

    * the token's resource owner is your user instead of the organization
    * the token has not been approved by an organization owner
    * the repository name or owner is wrong
    * the branch or directory path does not exist

This script isolates them for you. It runs a preflight repository probe before touching the
Trees API, so a failure tells you whether the problem is the credential, the repository, or
the path - rather than leaving you with an undiagnosable empty result.

Usage
-----
    python3 test-api.py --api-key <TOKEN> [options]

    Environment variables (CLI flags take precedence):
        GITHUB_TOKEN      Personal access token          (alternative to --api-key)
        GITHUB_URL        API base URL                   (alternative to --url)
        GITHUB_OWNER      Repository owner               (alternative to --owner)
        GITHUB_REPO       Repository name                (alternative to --repo)
        GITHUB_PATH       Directory path in the repo     (alternative to --path)
        GITHUB_BRANCH     Branch, tag, or commit SHA     (alternative to --branch)
        HTTPS_PROXY       Proxy URL                      (alternative to --proxy)

Optional flags:
    --url              Base API URL including scheme (default: https://api.github.com)
                       GitHub Enterprise Server: https://HOSTNAME/api/v3
                       GHEC with data residency:  https://api.SUBDOMAIN.ghe.com
    --owner            Repository owner       (default: elastic)
    --repo             Repository name        (default: security-advisories)
    --path             Directory to enumerate (default: advisories)
    --branch           Git ref to read        (default: main)
    --file-pattern     Glob matched against each file path relative to --path; repeatable.
                       Omit to collect everything.
    --max-pages        Stop after fetching N file blobs (default: 5). Safety limit so a
                       test run against a 500-file corpus does not fetch all 500.
    --skip-revalidate  Skip the conditional If-None-Match request.
    --timeout          HTTP request timeout in seconds (default: 60)
    --proxy            HTTP/HTTPS proxy URL
    --output-dir       Output directory name (default: test-api-output)
    --mock             Skip .tar.gz archiving; print the output directory path instead.

Output
------
On success the script creates an output directory containing:
    test-api.log             - verbose step-by-step log
    trace.json               - detailed request/response trace (auth redacted)

The directory is then archived as <output-dir>.tar.gz.
Please send this archive to the integration maintainers for review. The blob previews and
the detected-format summary it contains are what unblock the ingest pipeline design.
"""

import argparse
import base64
import fnmatch
import json
import logging
import os
import ssl
import sys
import tarfile
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request

GITHUB_API_VERSION = "2022-11-28"

LOG = logging.getLogger("test-api")
TRACE = []
_SECRETS = []


# --------------------------------------------------------------------------------------
# Redaction
# --------------------------------------------------------------------------------------

def register_secret(value):
    """Register a credential so it can be scrubbed from every output surface."""
    if value and value not in _SECRETS:
        _SECRETS.append(value)


def redact(text):
    """Replace every registered secret in *text* with [REDACTED]."""
    if not isinstance(text, str):
        return text
    for secret in _SECRETS:
        text = text.replace(secret, "[REDACTED]")
    return text


def redact_headers(headers):
    """Return a copy of *headers* with credential-bearing values replaced."""
    sensitive = {"authorization", "x-api-key", "cookie", "proxy-authorization"}
    return {
        key: ("[REDACTED]" if key.lower() in sensitive else redact(str(value)))
        for key, value in headers.items()
    }


def mask(value):
    """Mask a credential for display, keeping only the last 4 characters.

    The asterisk run is capped so a long token does not produce an unreadable line.
    """
    if not value:
        return "<not set>"
    if len(value) <= 4:
        return "****"
    return "%s%s (%d chars)" % ("*" * 12, value[-4:], len(value))


def _try_parse_body(text):
    """Return parsed JSON if *text* is valid JSON, otherwise the redacted string."""
    if not text:
        return text
    try:
        obj = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return redact(text)
    return obj


# --------------------------------------------------------------------------------------
# HTTP transport
# --------------------------------------------------------------------------------------

def build_opener(proxy, timeout):
    """Build a urllib opener with TLS verification disabled and optional proxy support."""
    # TLS verification is intentionally disabled: this is a diagnostic tool that may be
    # pointed at mock servers, GHES instances with private CAs, or intercepting proxies.
    context = ssl._create_unverified_context()
    handlers = [urllib.request.HTTPSHandler(context=context)]
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
    else:
        handlers.append(urllib.request.ProxyHandler({}))
    opener = urllib.request.build_opener(*handlers)
    opener.addheaders = []
    return opener


def do_request(opener, url, headers, timeout, step, description):
    """Perform one GET request and record it in the trace.

    Returns a dict with `status`, `headers`, `text`, `elapsed_s`, and `error`.
    A 304 Not Modified is returned as a normal result, not an error - it is the expected
    outcome of the revalidation step and the whole point of the ETag strategy.
    """
    request = urllib.request.Request(url, method="GET")
    for key, value in headers.items():
        request.add_header(key, value)

    entry = {
        "step": step,
        "description": description,
        "request": {
            "method": "GET",
            "url": redact(url),
            "headers": redact_headers(headers),
            "body": None,
        },
        "response": None,
        "error": None,
    }

    LOG.debug("Request %s: GET %s", step, redact(url))
    LOG.debug("Request %s headers: %s", step, redact_headers(headers))

    started = time.monotonic()
    try:
        with opener.open(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            elapsed = time.monotonic() - started
            result = {
                "status": response.status,
                "headers": dict(response.headers),
                "text": body,
                "elapsed_s": round(elapsed, 3),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        elapsed = time.monotonic() - started
        result = {
            "status": exc.code,
            "headers": dict(exc.headers) if exc.headers else {},
            "text": body,
            "elapsed_s": round(elapsed, 3),
            # A 304 arrives here because urllib treats any non-2xx as an HTTPError.
            "error": None if exc.code == 304 else "HTTP %d %s" % (exc.code, exc.reason),
        }
    except urllib.error.URLError as exc:
        elapsed = time.monotonic() - started
        result = {
            "status": None,
            "headers": {},
            "text": "",
            "elapsed_s": round(elapsed, 3),
            "error": "Connection error: %s" % redact(str(exc.reason)),
        }
    except Exception as exc:  # noqa: BLE001 - the script must never crash
        elapsed = time.monotonic() - started
        result = {
            "status": None,
            "headers": {},
            "text": "",
            "elapsed_s": round(elapsed, 3),
            "error": "%s: %s" % (type(exc).__name__, redact(str(exc))),
        }

    entry["response"] = {
        "status_code": result["status"],
        "headers": redact_headers(result["headers"]),
        "body": _try_parse_body(result["text"]),
        "elapsed_s": result["elapsed_s"],
    }
    entry["error"] = result["error"]
    TRACE.append(entry)

    LOG.debug(
        "Response %s: status=%s elapsed=%.3fs body_len=%d",
        step, result["status"], result["elapsed_s"], len(result["text"]),
    )
    log_rate_limit(result["headers"])
    if result["error"]:
        LOG.error("Request %s failed: %s", step, result["error"])
        if result["text"]:
            LOG.error("Response body: %s", redact(result["text"])[:2000])

    return result, entry


def log_rate_limit(headers):
    """Log GitHub's rate-limit headers when present."""
    interesting = [
        "x-ratelimit-limit", "x-ratelimit-remaining", "x-ratelimit-used",
        "x-ratelimit-reset", "x-ratelimit-resource", "retry-after",
    ]
    lowered = {key.lower(): value for key, value in headers.items()}
    present = {name: lowered[name] for name in interesting if name in lowered}
    if present:
        LOG.debug("Rate limit headers: %s", present)


def is_rate_limited(result):
    """GitHub signals both primary and secondary limits with 403 or 429.

    Status code is authoritative on its own: a secondary limit can return 429 while
    x-ratelimit-remaining is still non-zero and no retry-after header is present.
    """
    return result["status"] in (403, 429)


def report_rate_limit_and_stop(result):
    lowered = {key.lower(): value for key, value in result["headers"].items()}
    LOG.error("Rate limited (HTTP %s). Not retrying - this is a test tool.", result["status"])
    for name in ("retry-after", "x-ratelimit-remaining", "x-ratelimit-reset",
                 "x-ratelimit-limit", "x-ratelimit-resource"):
        if name in lowered:
            LOG.error("  %s: %s", name, lowered[name])
    print("  Rate limited (HTTP %s). See test-api.log for the rate-limit headers." % result["status"])


# --------------------------------------------------------------------------------------
# Content inspection
# --------------------------------------------------------------------------------------

def detect_format(text):
    """Best-effort classification of an advisory file's content format.

    The repository is private and its format was never observed during research, so this
    is the highest-value output of the script. Reported in the summary and the trace.
    """
    stripped = text.lstrip()
    if not stripped:
        return "empty"
    if stripped.startswith("{") or stripped.startswith("["):
        try:
            json.loads(text)
            return "json"
        except (json.JSONDecodeError, ValueError):
            return "json-like (did not parse)"
    if stripped.startswith("---"):
        # A YAML document marker, or YAML front matter followed by a Markdown body.
        rest = stripped[3:]
        if "\n---" in rest or "\n..." in rest:
            return "yaml-front-matter+markdown"
        return "yaml"
    if stripped.startswith("- "):
        return "yaml (sequence)"
    if stripped.startswith("#") or "\n## " in text or "**" in text:
        return "markdown"
    if ":" in stripped.split("\n", 1)[0]:
        return "yaml (mapping)"
    return "unknown/plain-text"


def decode_blob(body):
    """Decode a Git Blobs API response body into text.

    GitHub MIME-wraps the base64 payload with a newline every 60 characters. Python's
    b64decode discards non-alphabet characters by default, so no stripping is needed -
    the same is true of Go's base64.StdEncoding used by the CEL input's mito library.
    """
    if not isinstance(body, dict):
        return None, "response was not a JSON object"
    content = body.get("content")
    if content is None:
        return None, "no 'content' field in response"
    encoding = body.get("encoding")
    if encoding != "base64":
        return None, "unexpected encoding: %r" % (encoding,)
    try:
        return base64.b64decode(content).decode("utf-8", errors="replace"), None
    except Exception as exc:  # noqa: BLE001
        return None, "base64 decode failed: %s" % exc


# --------------------------------------------------------------------------------------
# Core collection - mirrors the proposed CEL program
# --------------------------------------------------------------------------------------

def run_collection(args, opener):
    """Execute the full proposed collection flow and return a summary dict.

    Flow, matching the CEL program design in the research brief:

        1. Preflight repository probe        (diagnostic only; not in the CEL program)
        2. Rate-limit probe                  (diagnostic only; not in the CEL program)
        3. Git Trees enumeration             -> CEL first request, populates state.cursor
        4. Conditional revalidation (ETag)   -> CEL steady-state poll; expects 304
        5. Git Blobs fetch loop              -> CEL want_more loop over changed blob SHAs
    """
    base = args.url.rstrip("/")
    repo_base = "%s/repos/%s/%s" % (base, args.owner, args.repo)

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
        "User-Agent": "elastic-security-advisories-test-api",
    }
    if args.api_key:
        headers["Authorization"] = "Bearer %s" % args.api_key

    summary = {
        "status": "FAILED",
        "repository_accessible": False,
        "default_branch": None,
        "private": None,
        "tree_entries": 0,
        "files_matched": 0,
        "truncated": False,
        "etag": None,
        "revalidation": None,
        "blobs_fetched": 0,
        "bytes_fetched": 0,
        "formats": {},
        "extensions": {},
        "rate_limit_before": None,
        "rate_limit_after": None,
        "errors": [],
    }

    # --- Step 1: preflight repository probe -------------------------------------------
    # Not part of the CEL program. It exists because every failure on this data source is
    # an identical 404, and this isolates "cannot see the repository" from "cannot see the
    # path" before the Trees call muddies the diagnosis.
    print("\n[1] Preflight: verifying repository access")
    result, _ = do_request(opener, repo_base, headers, args.timeout, "1-repo",
                           "Preflight repository probe")
    if result["error"] or result["status"] != 200:
        if is_rate_limited(result):
            report_rate_limit_and_stop(result)
            summary["errors"].append("rate limited during preflight")
            return summary
        print("    FAILED (HTTP %s, %.2fs)" % (result["status"], result["elapsed_s"]))
        if result["status"] == 404:
            print("    HTTP 404 on a private repository is ambiguous. Check, in order:")
            print("      a) Is the token's Resource owner set to '%s' and not your user account?" % args.owner)
            print("      b) Has an organization owner approved the token? (once-daily digest email)")
            print("      c) Are --owner '%s' and --repo '%s' correct?" % (args.owner, args.repo))
            print("      d) Can you browse the repository in a signed-in browser at all?")
        elif result["status"] == 401:
            print("    HTTP 401 means the token itself is malformed, revoked, or expired.")
        summary["errors"].append("preflight failed: HTTP %s" % result["status"])
        return summary

    repo_info = _try_parse_body(result["text"])
    if isinstance(repo_info, dict):
        summary["repository_accessible"] = True
        summary["default_branch"] = repo_info.get("default_branch")
        summary["private"] = repo_info.get("private")
        print("    OK (%.2fs) - private=%s, default_branch=%s"
              % (result["elapsed_s"], repo_info.get("private"), repo_info.get("default_branch")))
        if summary["default_branch"] and summary["default_branch"] != args.branch:
            print("    NOTE: --branch is '%s' but the repository default is '%s'."
                  % (args.branch, summary["default_branch"]))
        LOG.info("Repository accessible: private=%s default_branch=%s",
                 repo_info.get("private"), repo_info.get("default_branch"))

    # --- Step 2: rate-limit probe -----------------------------------------------------
    # Diagnostic only. GET /rate_limit does not count against the primary limit, which
    # lets us measure the cost of the revalidation step in step 4.
    print("\n[2] Checking rate-limit budget")
    result, _ = do_request(opener, "%s/rate_limit" % base, headers, args.timeout,
                           "2-ratelimit", "Rate limit probe")
    if result["status"] == 200:
        parsed = _try_parse_body(result["text"])
        core = parsed.get("resources", {}).get("core", {}) if isinstance(parsed, dict) else {}
        summary["rate_limit_before"] = core
        print("    OK - core: %s/%s remaining" % (core.get("remaining"), core.get("limit")))
        LOG.info("Rate limit core bucket: %s", core)
    else:
        print("    Skipped (HTTP %s) - not fatal" % result["status"])

    # --- Step 3: Git Trees enumeration ------------------------------------------------
    # This is the CEL program's first request. One call returns every file's path, size,
    # and blob SHA. The {ref}:{path} tree-ish form scopes recursion to the directory.
    tree_ref = "%s:%s" % (args.branch, args.path.strip("/"))
    tree_url = "%s/git/trees/%s?recursive=1" % (repo_base, urllib.parse.quote(tree_ref, safe=":"))
    print("\n[3] Enumerating '%s' at ref '%s' (Git Trees API)" % (args.path, args.branch))
    result, entry = do_request(opener, tree_url, headers, args.timeout, "3-tree",
                               "Git Trees enumeration")
    if result["error"] or result["status"] != 200:
        if is_rate_limited(result):
            report_rate_limit_and_stop(result)
            summary["errors"].append("rate limited during enumeration")
            return summary
        print("    FAILED (HTTP %s, %.2fs)" % (result["status"], result["elapsed_s"]))
        if result["status"] == 404:
            print("    The repository IS accessible, so this 404 means the ref or path is wrong.")
            print("      - Is --branch '%s' a real branch? (repository default is '%s')"
                  % (args.branch, summary["default_branch"]))
            print("      - Is --path '%s' correct? It must have no leading or trailing slash."
                  % args.path)
        summary["errors"].append("tree enumeration failed: HTTP %s" % result["status"])
        return summary

    tree_body = _try_parse_body(result["text"])
    etag = result["headers"].get("ETag") or result["headers"].get("etag")
    summary["etag"] = etag
    entries = tree_body.get("tree", []) if isinstance(tree_body, dict) else []
    summary["truncated"] = bool(tree_body.get("truncated")) if isinstance(tree_body, dict) else False
    summary["tree_entries"] = len(entries)

    blobs = [e for e in entries if e.get("type") == "blob"]
    matched = [e for e in blobs if matches_patterns(e.get("path", ""), args.file_pattern)]
    summary["files_matched"] = len(matched)

    entry["pagination"] = {
        "mechanism": "none (single-shot tree listing)",
        "field_used": "truncated",
        "value_from_response": summary["truncated"],
        "value_for_next_request": None,
        "want_more": False,
    }
    entry["event_count"] = len(matched)

    print("    OK (%.2fs) - %d tree entries, %d blobs, %d matched the file pattern"
          % (result["elapsed_s"], len(entries), len(blobs), len(matched)))
    print("    ETag: %s" % (etag or "<none returned>"))
    if summary["truncated"]:
        print("    WARNING: truncated=true. The listing is incomplete; fall back to")
        print("             per-subtree enumeration.")
    LOG.info("Tree: %d entries, %d blobs, %d matched, truncated=%s, etag=%s",
             len(entries), len(blobs), len(matched), summary["truncated"], etag)

    for item in matched[:50]:
        LOG.debug("  matched: %s (sha=%s size=%s)",
                  item.get("path"), item.get("sha"), item.get("size"))

    # --- Step 4: conditional revalidation ---------------------------------------------
    # This is the CEL program's steady-state poll. A 304 on an authorized conditional
    # request consumes zero rate-limit budget, which is what makes a 1h interval free.
    if etag and not args.skip_revalidate:
        print("\n[4] Revalidating the listing with If-None-Match (expect HTTP 304)")
        cond_headers = dict(headers)
        cond_headers["If-None-Match"] = etag
        result2, entry2 = do_request(opener, tree_url, cond_headers, args.timeout,
                                     "4-revalidate", "Conditional revalidation")
        entry2["pagination"] = {
            "mechanism": "etag revalidation",
            "field_used": "If-None-Match request header / ETag response header",
            "value_from_response": etag,
            "value_for_next_request": etag,
            "want_more": False,
        }
        if result2["status"] == 304:
            summary["revalidation"] = "304 Not Modified"
            print("    OK (%.2fs) - HTTP 304, listing unchanged" % result2["elapsed_s"])
            # Compare x-ratelimit-used on the 200 that produced the ETag against the same
            # header on the 304. Anchoring on the earlier /rate_limit probe instead would
            # fold the cost of the tree request itself into the delta.
            used_before = {k.lower(): v for k, v in result["headers"].items()}.get("x-ratelimit-used")
            used_after = {k.lower(): v for k, v in result2["headers"].items()}.get("x-ratelimit-used")
            if used_before is not None and used_after is not None:
                free = str(used_before) == str(used_after)
                summary["revalidation_was_free"] = free
                print("    x-ratelimit-used: %s on the 200 -> %s on the 304%s"
                      % (used_before, used_after,
                         "  (conditional request was free)" if free
                         else "  (unexpected: the 304 consumed budget)"))
            LOG.info("Revalidation returned 304 as expected (used %s -> %s)",
                     used_before, used_after)
        else:
            summary["revalidation"] = "HTTP %s" % result2["status"]
            print("    Unexpected: HTTP %s (expected 304). Conditional requests may not be"
                  % result2["status"])
            print("    honoured here; the zero-cost polling property would not hold.")
            LOG.warning("Revalidation returned HTTP %s, expected 304", result2["status"])
    elif args.skip_revalidate:
        print("\n[4] Revalidation skipped (--skip-revalidate)")
    else:
        print("\n[4] Revalidation skipped - no ETag was returned")

    # --- Step 5: Git Blobs fetch loop -------------------------------------------------
    # This is the CEL program's want_more loop. In production it fetches only blobs whose
    # SHA is new or changed versus the persisted path -> sha map; here it fetches the
    # first --max-pages files so a test run does not pull the whole corpus.
    to_fetch = matched[: args.max_pages]
    print("\n[5] Fetching file contents (Git Blobs API), %d of %d matched files"
          % (len(to_fetch), len(matched)))
    if not to_fetch:
        print("    Nothing to fetch.")
        if blobs and not matched:
            print("    %d blobs exist but none matched --file-pattern %s"
                  % (len(blobs), args.file_pattern))

    for index, item in enumerate(to_fetch, start=1):
        path = item.get("path", "")
        sha = item.get("sha", "")
        blob_url = item.get("url") or "%s/git/blobs/%s" % (repo_base, sha)
        result3, entry3 = do_request(opener, blob_url, headers, args.timeout,
                                     "5-blob-%d" % index, "Git blob fetch: %s" % path)
        entry3["pagination"] = {
            "mechanism": "blob worklist from the tree listing",
            "field_used": "tree[].sha",
            "value_from_response": sha,
            "value_for_next_request": None,
            "want_more": index < len(to_fetch),
        }
        entry3["file_path"] = path

        if result3["error"] or result3["status"] != 200:
            if is_rate_limited(result3):
                report_rate_limit_and_stop(result3)
                summary["errors"].append("rate limited fetching %s" % path)
                break
            print("    [%d/%d] %s -> FAILED (HTTP %s)"
                  % (index, len(to_fetch), path, result3["status"]))
            summary["errors"].append("blob fetch failed for %s: HTTP %s" % (path, result3["status"]))
            continue

        body = _try_parse_body(result3["text"])
        text, decode_error = decode_blob(body)
        if decode_error:
            print("    [%d/%d] %s -> decoded FAILED (%s)"
                  % (index, len(to_fetch), path, decode_error))
            entry3["decode_error"] = decode_error
            summary["errors"].append("decode failed for %s: %s" % (path, decode_error))
            continue

        fmt = detect_format(text)
        ext = os.path.splitext(path)[1] or "<none>"
        summary["blobs_fetched"] += 1
        summary["bytes_fetched"] += len(text)
        summary["formats"][fmt] = summary["formats"].get(fmt, 0) + 1
        summary["extensions"][ext] = summary["extensions"].get(ext, 0) + 1

        # The decoded preview is the payload that answers the open question about the
        # repository's on-disk advisory format. It is deliberately generous.
        entry3["decoded"] = {
            "path": path,
            "blob_sha": sha,
            "bytes": len(text),
            "detected_format": fmt,
            "first_line": text.split("\n", 1)[0][:300],
            "preview": text[:4000],
            "truncated_preview": len(text) > 4000,
        }
        entry3["event_count"] = 1

        print("    [%d/%d] %s -> OK (%.2fs, %d bytes, format=%s)"
              % (index, len(to_fetch), path, result3["elapsed_s"], len(text), fmt))
        LOG.info("Blob %s: %d bytes, format=%s, sha=%s", path, len(text), fmt, sha)
        LOG.debug("Blob %s first line: %s", path, text.split("\n", 1)[0][:300])

    # --- Final rate-limit reading -----------------------------------------------------
    result4, _ = do_request(opener, "%s/rate_limit" % base, headers, args.timeout,
                            "6-ratelimit", "Final rate limit probe")
    if result4["status"] == 200:
        parsed = _try_parse_body(result4["text"])
        if isinstance(parsed, dict):
            summary["rate_limit_after"] = parsed.get("resources", {}).get("core", {})

    if summary["blobs_fetched"] > 0 and not summary["errors"]:
        summary["status"] = "SUCCESS"
    elif summary["blobs_fetched"] > 0:
        summary["status"] = "PARTIAL"

    return summary


def matches_patterns(path, patterns):
    """Return True if *path* matches any glob in *patterns*, or if *patterns* is empty."""
    if not patterns:
        return True
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


# --------------------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------------------

def print_summary(summary, args):
    print("\n" + "=" * 78)
    print("EXECUTION SUMMARY")
    print("=" * 78)
    print("  Status:                %s" % summary["status"])
    print("  Repository accessible: %s" % summary["repository_accessible"])
    print("  Repository private:    %s" % summary["private"])
    print("  Default branch:        %s" % summary["default_branch"])
    print("  Tree entries:          %d" % summary["tree_entries"])
    print("  Files matched:         %d" % summary["files_matched"])
    print("  Listing truncated:     %s" % summary["truncated"])
    print("  Revalidation:          %s" % (summary["revalidation"] or "not attempted"))
    print("  Blobs fetched:         %d (%d bytes)"
          % (summary["blobs_fetched"], summary["bytes_fetched"]))

    if summary["extensions"]:
        print("\n  File extensions observed:")
        for ext, count in sorted(summary["extensions"].items(), key=lambda kv: -kv[1]):
            print("      %-12s %d" % (ext, count))

    if summary["formats"]:
        print("\n  Detected content formats:")
        for fmt, count in sorted(summary["formats"].items(), key=lambda kv: -kv[1]):
            print("      %-28s %d" % (fmt, count))
        print("\n  ^ This is the answer to the largest open question in the research brief.")

    before = (summary["rate_limit_before"] or {}).get("remaining")
    after = (summary["rate_limit_after"] or {}).get("remaining")
    if before is not None and after is not None:
        print("\n  Rate limit remaining:  %s -> %s (consumed %s)"
              % (before, after, int(before) - int(after)))

    if summary["errors"]:
        print("\n  Errors (%d):" % len(summary["errors"]))
        for message in summary["errors"][:20]:
            print("      - %s" % message)

    if summary["files_matched"] > summary["blobs_fetched"]:
        print("\n  Note: only the first %d files were fetched (--max-pages). Raise it to"
              % args.max_pages)
        print("        sample more of the corpus.")


def write_outputs(output_dir, summary):
    trace_path = os.path.join(output_dir, "trace.json")
    with open(trace_path, "w", encoding="utf-8") as handle:
        json.dump({"summary": summary, "exchanges": TRACE}, handle, indent=2, default=str)
    LOG.info("Wrote trace to %s", trace_path)
    return trace_path


def archive_output(output_dir):
    archive_path = "%s.tar.gz" % output_dir
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(output_dir, arcname=os.path.basename(output_dir))
    return archive_path


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Test the GitHub API flow proposed for the elastic_security_advisories "
                    "integration.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--api-key", default=os.environ.get("GITHUB_TOKEN"),
                        help="GitHub personal access token (env: GITHUB_TOKEN)")
    parser.add_argument("--url", default=os.environ.get("GITHUB_URL", "https://api.github.com"),
                        help="Base API URL including scheme (env: GITHUB_URL)")
    parser.add_argument("--owner", default=os.environ.get("GITHUB_OWNER", "elastic"),
                        help="Repository owner (env: GITHUB_OWNER)")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPO", "security-advisories"),
                        help="Repository name (env: GITHUB_REPO)")
    parser.add_argument("--path", default=os.environ.get("GITHUB_PATH", "advisories"),
                        help="Directory path inside the repository (env: GITHUB_PATH)")
    parser.add_argument("--branch", default=os.environ.get("GITHUB_BRANCH", "main"),
                        help="Branch, tag, or commit SHA (env: GITHUB_BRANCH)")
    parser.add_argument("--file-pattern", action="append", default=None,
                        help="Glob matched against file paths; repeatable. Omit for all files.")
    parser.add_argument("--max-pages", type=int, default=5,
                        help="Stop after fetching N file blobs (default: 5)")
    parser.add_argument("--skip-revalidate", action="store_true",
                        help="Skip the conditional If-None-Match request")
    parser.add_argument("--timeout", type=int, default=60,
                        help="HTTP request timeout in seconds (default: 60)")
    parser.add_argument("--proxy", default=os.environ.get("HTTPS_PROXY"),
                        help="HTTP/HTTPS proxy URL (env: HTTPS_PROXY)")
    parser.add_argument("--output-dir", default="test-api-output",
                        help="Output directory name (default: test-api-output)")
    parser.add_argument("--mock", action="store_true",
                        help="Skip .tar.gz archiving; print the output directory path")
    return parser.parse_args(argv)


def setup_logging(output_dir):
    log_path = os.path.join(output_dir, "test-api.log")
    LOG.setLevel(logging.DEBUG)
    LOG.handlers = []
    handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)-7s %(message)s", datefmt="%Y-%m-%dT%H:%M:%S"))
    LOG.addHandler(handler)
    return log_path


def main(argv=None):
    args = parse_args(argv if argv is not None else sys.argv[1:])
    register_secret(args.api_key)

    print("=" * 78)
    print("Elastic Security Advisories - GitHub repository file collection test")
    print("Exercises the Git Trees + Git Blobs flow proposed for the CEL integration.")
    print("=" * 78)
    print("  Base URL:        %s" % args.url)
    print("  Repository:      %s/%s" % (args.owner, args.repo))
    print("  Directory:       %s" % args.path)
    print("  Ref:             %s" % args.branch)
    print("  Token:           %s" % mask(args.api_key))
    print("  File pattern:    %s" % (args.file_pattern or "<all files>"))
    print("  Max files:       %d" % args.max_pages)
    print("  Timeout:         %ds" % args.timeout)
    print("  Proxy:           %s" % (args.proxy or "<none>"))

    if not args.api_key:
        print("\n  WARNING: no token supplied. Unauthenticated requests are limited to 60/hour")
        print("           and cannot read a private repository. Pass --api-key or set")
        print("           GITHUB_TOKEN.")

    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    log_path = setup_logging(output_dir)
    LOG.info("Configuration: url=%s owner=%s repo=%s path=%s branch=%s "
             "file_pattern=%s max_pages=%d timeout=%d proxy=%s token=%s",
             args.url, args.owner, args.repo, args.path, args.branch,
             args.file_pattern, args.max_pages, args.timeout, args.proxy or "<none>",
             mask(args.api_key))

    opener = build_opener(args.proxy, args.timeout)

    summary = None
    exit_code = 1
    try:
        summary = run_collection(args, opener)
        exit_code = 0 if summary["status"] == "SUCCESS" else 1
    except KeyboardInterrupt:
        LOG.warning("Interrupted by user")
        print("\n  Interrupted. Writing partial output.")
        summary = summary or {"status": "INTERRUPTED", "errors": ["interrupted by user"]}
    except Exception as exc:  # noqa: BLE001 - the script must never crash
        LOG.error("Unhandled exception: %s", redact(str(exc)))
        LOG.error("%s", redact(traceback.format_exc()))
        print("\n  Unexpected error: %s" % redact(str(exc)))
        print("  Full traceback is in %s" % log_path)
        summary = summary or {"status": "FAILED", "errors": [redact(str(exc))]}

    summary = summary or {"status": "FAILED", "errors": ["no summary produced"]}
    summary.setdefault("errors", [])
    for key, default in (("repository_accessible", False), ("private", None),
                         ("default_branch", None), ("tree_entries", 0),
                         ("files_matched", 0), ("truncated", False),
                         ("revalidation", None), ("blobs_fetched", 0),
                         ("bytes_fetched", 0), ("formats", {}), ("extensions", {}),
                         ("rate_limit_before", None), ("rate_limit_after", None)):
        summary.setdefault(key, default)

    try:
        write_outputs(output_dir, summary)
    except Exception as exc:  # noqa: BLE001
        print("  Failed to write trace.json: %s" % exc)
        LOG.error("Failed to write trace.json: %s", exc)

    print_summary(summary, args)
    LOG.info("Summary: %s", summary)

    print("\n" + "-" * 78)
    if args.mock:
        print("Mock mode: archiving skipped.")
        print("Output directory: %s" % output_dir)
        print("  test-api.log  - verbose step-by-step log")
        print("  trace.json    - full request/response trace, including decoded file previews")
    else:
        try:
            archive_path = archive_output(output_dir)
            print("Archive created: %s" % archive_path)
            print("Please send this archive to the integration maintainers. It contains the")
            print("decoded advisory file previews that unblock the ingest pipeline design.")
        except Exception as exc:  # noqa: BLE001
            LOG.error("Archiving failed: %s", exc)
            print("Archiving failed (%s)." % exc)
            print("Send the unarchived directory instead: %s" % output_dir)
    print("-" * 78)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
