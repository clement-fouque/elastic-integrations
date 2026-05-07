#!/usr/bin/env python3
"""
HackerOne — API Connectivity & Flow Test
========================================

Standalone test client that exercises the exact polling flow proposed for the
Elastic Agent `hackerone` integration's `report` data stream against the
HackerOne Customer API (https://api.hackerone.com/v1/reports). Use it to
validate connectivity, HTTP Basic authentication, page-number pagination,
time-range filtering with `filter[last_activity_at__gt]`, and the actual
JSON:API response shape against a real (or mocked) HackerOne tenant before
any Elastic Agent / CEL work is undertaken.

Vendor-side setup
-----------------
HackerOne API tokens are issued at the **organization** level (not per-user)
and require a Professional, Community, Enterprise, or Sandbox program.

1. Sign in to HackerOne (https://hackerone.com) as an **Organization
   Administrator** of the program you want to read reports from.

2. Open **Organization Settings → API Tokens**. (Direct URL pattern:
   https://hackerone.com/organizations/<your_org>/api_tokens)

3. Click **Create API Token**.
   - Give it a meaningful name (e.g. "Elastic Agent — reports read-only").
   - Assign it to a token group whose permission set includes at least
     **`report_management`**. Read access to reports is sufficient for this
     script and for the polling integration; write permissions are NOT
     required.
   - Copy the **Identifier** and **Value** that HackerOne shows on creation.
     The **Value** is shown only once. Treat both as sensitive secrets.

4. Identify the **program handle(s)** to poll. The handle is the slug used
   in the program's public URL: `https://hackerone.com/<handle>`. Examples:
   `security`, `acme-bug-bounty`, `your-org`. You can supply multiple
   handles via repeated `--program` flags or a comma-separated env var.

5. (Optional) If your organization enforces **IP allowlisting on API
   tokens**, add the egress IP of the host running this script (and later
   the Elastic Agent) to the allowlist. Otherwise the API will return
   403 Forbidden even with a valid token.

6. (Optional) If you only want to query a subset of inboxes instead of
   whole programs, use `--inbox-id` (repeatable) instead of `--program`.
   Either is required by the API; you may supply both.

Authentication wire format
--------------------------
    Authorization: Basic <base64("<token_identifier>:<token_value>")>
    Accept: application/json

This script always sends `Accept: application/json` (matching the official
docs) and HTTP Basic credentials per request.

Usage
-----
    python3 test-api.py \\
        --api-token-identifier <ID> \\
        --api-token-value <VALUE> \\
        --program <handle> [--program <handle> ...] \\
        [optional flags]

Environment variables (alternative to CLI flags):
    HACKERONE_API_TOKEN_IDENTIFIER  (alternative to --api-token-identifier)
    HACKERONE_API_TOKEN_VALUE       (alternative to --api-token-value)
    HACKERONE_URL                   (alternative to --url)
    HACKERONE_PROGRAMS              (comma-separated; alternative to repeated --program)
    HACKERONE_INBOX_IDS             (comma-separated; alternative to repeated --inbox-id)
    HTTPS_PROXY                     (alternative to --proxy)

CLI takes precedence over the environment.

Optional flags:
    --url               Base API URL including scheme (default: https://api.hackerone.com)
    --initial-interval  Initial lookback for the first page request (default: 24h).
                        Maps to `filter[last_activity_at__gt] = now - <interval>`.
                        Accepted suffixes: s, m, h, d.
    --page-size         Reports per page (default: 100; API max: 100, min: 1).
    --max-pages         Stop after N pages (default: 5). Test-only safety cap.
    --state             Repeatable. Restrict to one or more report states
                        (new, pending-program-review, triaged, needs-more-info,
                        resolved, not-applicable, informative, duplicate,
                        spam, retesting). Empty = all.
    --severity          Repeatable. Restrict to one or more severities
                        (none, low, medium, high, critical). Empty = all.
    --timeout           HTTP request timeout in seconds (default: 60).
    --proxy             HTTP/HTTPS proxy URL.
    --output-dir        Output directory name (default: test-api-output).
    --mock              Skip archive creation; print output directory path
                        (used by the CEL builder agent for local mock-server
                        validation).

Output
------
On success the script writes an output directory containing:
    test-api.log   — verbose step-by-step log (auth redacted)
    trace.json     — detailed request/response trace with parsed bodies,
                     pagination state transitions (auth redacted)

In default mode the directory is then archived as <output-dir>.tar.gz —
please attach this archive when handing the result back to the integration
maintainers. In `--mock` mode the archive step is skipped and the absolute
path of the output directory is printed instead.

Exits 0 on success and 1 on any failure. TLS verification is disabled —
this is a testing tool, not a production client.
"""

import argparse
import base64
import datetime as _dt
import json
import logging
import os
import re
import shutil
import ssl
import sys
import tarfile
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request


REDACTION_PLACEHOLDER = "[REDACTED]"

VALID_STATES = {
    "new",
    "pending-program-review",
    "triaged",
    "needs-more-info",
    "resolved",
    "not-applicable",
    "informative",
    "duplicate",
    "spam",
    "retesting",
}

VALID_SEVERITIES = {"none", "low", "medium", "high", "critical"}


def _csv_to_list(value):
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_interval(text):
    """Parse a human-readable interval string like `24h`, `30m`, `7d` into seconds."""
    if text is None:
        raise ValueError("Interval is required")
    match = re.fullmatch(r"\s*(\d+)\s*([smhd])?\s*", text)
    if not match:
        raise ValueError(
            "Invalid interval %r — expected an integer followed by an optional unit (s/m/h/d)" % text
        )
    value = int(match.group(1))
    unit = match.group(2) or "s"
    multiplier = {"s": 1, "m": 60, "h": 3600, "d": 86400}[unit]
    return value * multiplier


def iso8601_utc(timestamp):
    """Format a Unix epoch seconds value as an ISO 8601 UTC string with millisecond precision."""
    dt = _dt.datetime.fromtimestamp(timestamp, tz=_dt.timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.") + ("%03d" % (dt.microsecond // 1000)) + "Z"


def mask_secret(value):
    """Return a masked version of *value* showing only the last 4 characters."""
    if not value:
        return ""
    if len(value) <= 4:
        return "*" * len(value)
    return ("*" * (len(value) - 4)) + value[-4:]


def basic_auth_header(token_identifier, token_value):
    raw = ("%s:%s" % (token_identifier, token_value)).encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def redact_headers(headers):
    """Return a shallow copy of *headers* with sensitive values redacted."""
    if not headers:
        return {}
    redacted = {}
    for key, value in headers.items():
        if key.lower() == "authorization":
            redacted[key] = REDACTION_PLACEHOLDER
        else:
            redacted[key] = value
    return redacted


def redact_url(url, sensitive_substrings):
    """Replace any occurrence of a sensitive substring inside *url* with [REDACTED]."""
    if not url:
        return url
    sanitized = url
    for token in sensitive_substrings:
        if token:
            sanitized = sanitized.replace(token, REDACTION_PLACEHOLDER)
    return sanitized


def _try_parse_body(text):
    """Return parsed JSON object if *text* is valid JSON, otherwise the raw string."""
    if not text:
        return text
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return text


# ----- HTTP transport -------------------------------------------------------


class HTTPClient:
    """Minimal urllib-based HTTP client used to mirror the proposed CEL polling flow."""

    def __init__(self, timeout, proxy_url, logger):
        self.timeout = timeout
        self.logger = logger
        # TLS verification is intentionally disabled. This is a testing tool that
        # may be pointed at mock servers, regional endpoints, or proxies with
        # self-signed certs. Do NOT copy this pattern to production code.
        self.ssl_context = ssl._create_unverified_context()

        handlers = []
        if proxy_url:
            handlers.append(urllib.request.ProxyHandler({"http": proxy_url, "https": proxy_url}))
        else:
            # Disable any environment-derived proxy auto-discovery so the only
            # proxy in effect is whatever the user explicitly configured.
            handlers.append(urllib.request.ProxyHandler({}))
        handlers.append(urllib.request.HTTPSHandler(context=self.ssl_context))
        self.opener = urllib.request.build_opener(*handlers)

    def request(self, method, url, headers, body=None):
        """Send a single HTTP request and return (status_code, response_headers_dict, body_text, elapsed_s)."""
        request = urllib.request.Request(url=url, method=method, data=body)
        for key, value in headers.items():
            request.add_header(key, value)
        start = time.monotonic()
        try:
            with self.opener.open(request, timeout=self.timeout) as response:
                response_headers = dict(response.headers.items())
                body_bytes = response.read()
                status_code = response.getcode()
        except urllib.error.HTTPError as http_err:
            response_headers = dict(http_err.headers.items()) if http_err.headers else {}
            try:
                body_bytes = http_err.read()
            except Exception:  # pragma: no cover — defensive
                body_bytes = b""
            status_code = http_err.code
        elapsed_s = time.monotonic() - start
        try:
            body_text = body_bytes.decode("utf-8", errors="replace")
        except Exception:  # pragma: no cover — defensive
            body_text = ""
        return status_code, response_headers, body_text, elapsed_s


# ----- Core collection loop -------------------------------------------------


def build_query(programs, inbox_ids, last_activity_after, page_number, page_size, states, severities):
    """Build the query parameter list for GET /v1/reports.

    Mirrors the CEL program: required `filter[program][]` or `filter[inbox_ids][]`,
    `filter[last_activity_at__gt]` cursor, ascending sort by
    `reports.last_activity_at`, page-number pagination.
    """
    params = []
    for handle in programs:
        params.append(("filter[program][]", handle))
    for inbox_id in inbox_ids:
        params.append(("filter[inbox_ids][]", str(inbox_id)))
    if last_activity_after:
        params.append(("filter[last_activity_at__gt]", last_activity_after))
    for state in states:
        params.append(("filter[state][]", state))
    for severity in severities:
        params.append(("filter[severity][]", severity))
    params.append(("page[number]", str(page_number)))
    params.append(("page[size]", str(page_size)))
    params.append(("sort", "reports.last_activity_at"))
    return params


def collect(args, http, logger, sensitive_values):
    """Run the paginated collection loop and return the trace + summary stats."""
    trace = []
    pages_fetched = 0
    total_events = 0
    state_counts = {}
    severity_counts = {}
    cursor_advance = None
    auth_header = basic_auth_header(args.api_token_identifier, args.api_token_value)
    headers = {
        "Authorization": auth_header,
        "Accept": "application/json",
        "User-Agent": "elastic-hackerone-test-api/1.0 (+https://github.com/elastic/integrations)",
    }

    initial_seconds = parse_interval(args.initial_interval)
    last_activity_after = iso8601_utc(time.time() - initial_seconds)
    logger.info("Initial cursor (filter[last_activity_at__gt]) = %s", last_activity_after)

    page_number = 1
    while page_number <= args.max_pages:
        params = build_query(
            programs=args.program,
            inbox_ids=args.inbox_id,
            last_activity_after=last_activity_after,
            page_number=page_number,
            page_size=args.page_size,
            states=args.state,
            severities=args.severity,
        )
        query_string = urllib.parse.urlencode(params, doseq=True)
        url = args.url.rstrip("/") + "/v1/reports?" + query_string

        logger.info("[%d/%d] Requesting page %d", page_number, args.max_pages, page_number)
        print("[%d/%d] Requesting page %d ..." % (page_number, args.max_pages, page_number), flush=True)

        entry = {
            "page": page_number,
            "request": {
                "method": "GET",
                "url": redact_url(url, sensitive_values),
                "headers": redact_headers(headers),
                "body": None,
            },
            "response": None,
            "pagination": {
                "mechanism": "page_number",
                "field_used": "links.next",
                "value_from_response": None,
                "value_for_next_request": None,
                "want_more": False,
            },
            "event_count": 0,
            "error": None,
        }

        try:
            status_code, response_headers, body_text, elapsed_s = http.request(
                "GET", url, headers
            )
        except urllib.error.URLError as url_err:
            err_text = "URLError: %s" % url_err.reason
            logger.error("Page %d failed: %s", page_number, err_text)
            print("[%d/%d] FAILED (%s)" % (page_number, args.max_pages, err_text), flush=True)
            entry["error"] = {"type": "URLError", "message": str(url_err.reason)}
            entry["response"] = {"status_code": None, "headers": {}, "body": None, "elapsed_s": None}
            trace.append(entry)
            return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, False
        except Exception as exc:
            err_text = "%s: %s" % (type(exc).__name__, exc)
            logger.error("Page %d failed: %s", page_number, err_text)
            logger.debug("Traceback:\n%s", traceback.format_exc())
            print("[%d/%d] FAILED (%s)" % (page_number, args.max_pages, err_text), flush=True)
            entry["error"] = {"type": type(exc).__name__, "message": str(exc)}
            entry["response"] = {"status_code": None, "headers": {}, "body": None, "elapsed_s": None}
            trace.append(entry)
            return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, False

        body_obj = _try_parse_body(body_text)
        entry["response"] = {
            "status_code": status_code,
            "headers": response_headers,
            "body": body_obj,
            "elapsed_s": round(elapsed_s, 4),
        }

        if status_code == 429:
            retry_after = response_headers.get("Retry-After") or response_headers.get("retry-after")
            rl_remaining = response_headers.get("X-RateLimit-Remaining") or response_headers.get("x-ratelimit-remaining")
            rl_reset = response_headers.get("X-RateLimit-Reset") or response_headers.get("x-ratelimit-reset")
            logger.error(
                "Rate limited (HTTP 429). Retry-After=%r, X-RateLimit-Remaining=%r, X-RateLimit-Reset=%r",
                retry_after,
                rl_remaining,
                rl_reset,
            )
            print(
                "[%d/%d] FAILED (HTTP 429 — rate limited; Retry-After=%s)"
                % (page_number, args.max_pages, retry_after),
                flush=True,
            )
            entry["error"] = {
                "type": "RateLimited",
                "message": "HTTP 429",
                "retry_after": retry_after,
            }
            trace.append(entry)
            return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, False

        if status_code < 200 or status_code >= 300:
            logger.error("HTTP %d on page %d (%.2fs)", status_code, page_number, elapsed_s)
            print(
                "[%d/%d] FAILED (HTTP %d, %.2fs)" % (page_number, args.max_pages, status_code, elapsed_s),
                flush=True,
            )
            entry["error"] = {"type": "HTTPError", "message": "HTTP %d" % status_code}
            trace.append(entry)
            return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, False

        if not isinstance(body_obj, dict) or "data" not in body_obj or not isinstance(body_obj.get("data"), list):
            logger.error("Page %d response is not a JSON:API list envelope", page_number)
            print(
                "[%d/%d] FAILED (response is not {data: [...]})"
                % (page_number, args.max_pages),
                flush=True,
            )
            entry["error"] = {
                "type": "MalformedResponse",
                "message": "Response top-level is not a JSON object with an array under 'data'",
            }
            trace.append(entry)
            return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, False

        data_array = body_obj.get("data") or []
        entry["event_count"] = len(data_array)
        pages_fetched += 1
        total_events += len(data_array)

        for record in data_array:
            attrs = (record or {}).get("attributes") or {}
            state = attrs.get("state")
            if state:
                state_counts[state] = state_counts.get(state, 0) + 1
            severity_node = (
                ((record or {}).get("relationships") or {})
                .get("severity", {})
                .get("data", {})
            )
            if isinstance(severity_node, dict):
                rating = (severity_node.get("attributes") or {}).get("rating")
                if rating:
                    severity_counts[rating] = severity_counts.get(rating, 0) + 1
            last_activity_at = attrs.get("last_activity_at") or attrs.get("created_at")
            if last_activity_at and (cursor_advance is None or last_activity_at > cursor_advance):
                cursor_advance = last_activity_at

        links_next = (body_obj.get("links") or {}).get("next")
        want_more = bool(links_next) and len(data_array) >= args.page_size

        entry["pagination"]["value_from_response"] = links_next
        entry["pagination"]["want_more"] = want_more

        if want_more:
            entry["pagination"]["value_for_next_request"] = "page[number]=%d" % (page_number + 1)
        else:
            entry["pagination"]["value_for_next_request"] = None

        time_span = ""
        if data_array:
            first_attrs = (data_array[0] or {}).get("attributes") or {}
            last_attrs = (data_array[-1] or {}).get("attributes") or {}
            first_ts = first_attrs.get("last_activity_at") or first_attrs.get("created_at")
            last_ts = last_attrs.get("last_activity_at") or last_attrs.get("created_at")
            if first_ts and last_ts:
                time_span = " span=[%s … %s]" % (first_ts, last_ts)
        suffix = " more pages available" if want_more else " no more pages"
        print(
            "[%d/%d] OK (%d events, %.2fs)%s%s"
            % (page_number, args.max_pages, len(data_array), elapsed_s, time_span, suffix),
            flush=True,
        )
        logger.info(
            "Page %d returned %d events in %.3fs (status=%d, links.next present=%s)",
            page_number,
            len(data_array),
            elapsed_s,
            status_code,
            bool(links_next),
        )
        trace.append(entry)

        if not want_more:
            return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, True

        page_number += 1
        time.sleep(0.2)

    logger.info("Reached --max-pages=%d safety cap; stopping.", args.max_pages)
    print(
        "Reached --max-pages=%d safety cap; stopping pagination." % args.max_pages,
        flush=True,
    )
    return trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, True


# ----- Output writing -------------------------------------------------------


def write_outputs(output_dir, trace):
    trace_path = os.path.join(output_dir, "trace.json")
    with open(trace_path, "w", encoding="utf-8") as fh:
        json.dump(trace, fh, indent=2, sort_keys=False, default=str)
    return trace_path


def archive_output_dir(output_dir):
    archive_path = output_dir.rstrip(os.sep) + ".tar.gz"
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(output_dir, arcname=os.path.basename(output_dir.rstrip(os.sep)))
    return archive_path


# ----- Main -----------------------------------------------------------------


def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="HackerOne /v1/reports connectivity & flow test (read-only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--api-token-identifier",
        default=os.environ.get("HACKERONE_API_TOKEN_IDENTIFIER"),
        help="HackerOne API token identifier (HTTP Basic username). "
             "Env: HACKERONE_API_TOKEN_IDENTIFIER",
    )
    parser.add_argument(
        "--api-token-value",
        default=os.environ.get("HACKERONE_API_TOKEN_VALUE"),
        help="HackerOne API token value (HTTP Basic password). "
             "Env: HACKERONE_API_TOKEN_VALUE",
    )
    parser.add_argument(
        "--url",
        default=os.environ.get("HACKERONE_URL", "https://api.hackerone.com"),
        help="Base API URL including scheme. Default: https://api.hackerone.com",
    )
    parser.add_argument(
        "--program",
        action="append",
        default=None,
        help="Program handle to query (repeatable). Either --program or --inbox-id is required by the API. "
             "Env: HACKERONE_PROGRAMS (comma-separated)",
    )
    parser.add_argument(
        "--inbox-id",
        action="append",
        default=None,
        help="Inbox ID to query (repeatable). Either --program or --inbox-id is required by the API. "
             "Env: HACKERONE_INBOX_IDS (comma-separated)",
    )
    parser.add_argument(
        "--initial-interval",
        default="24h",
        help="First-poll lookback (e.g. 24h, 7d). Default: 24h.",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=100,
        help="Reports per page (default: 100; API max: 100).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=5,
        help="Stop after N pages (default: 5).",
    )
    parser.add_argument(
        "--state",
        action="append",
        default=None,
        help="Restrict to one or more report states (repeatable). Allowed: %s"
             % ", ".join(sorted(VALID_STATES)),
    )
    parser.add_argument(
        "--severity",
        action="append",
        default=None,
        help="Restrict to one or more severities (repeatable). Allowed: %s"
             % ", ".join(sorted(VALID_SEVERITIES)),
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="HTTP request timeout in seconds (default: 60).",
    )
    parser.add_argument(
        "--proxy",
        default=os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY"),
        help="HTTP/HTTPS proxy URL. Env: HTTPS_PROXY",
    )
    parser.add_argument(
        "--output-dir",
        default="test-api-output",
        help="Output directory name (default: test-api-output).",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Mock mode: skip .tar.gz archiving and print the output directory path.",
    )
    return parser


def normalize_args(args):
    """Resolve env-variable list inputs and validate values."""
    if not args.program:
        args.program = _csv_to_list(os.environ.get("HACKERONE_PROGRAMS", ""))
    if not args.inbox_id:
        args.inbox_id = _csv_to_list(os.environ.get("HACKERONE_INBOX_IDS", ""))

    args.state = list(args.state or [])
    args.severity = list(args.severity or [])

    bad_states = [s for s in args.state if s not in VALID_STATES]
    if bad_states:
        raise ValueError("Unknown report state(s): %s" % ", ".join(bad_states))
    bad_severities = [s for s in args.severity if s not in VALID_SEVERITIES]
    if bad_severities:
        raise ValueError("Unknown severity value(s): %s" % ", ".join(bad_severities))

    if args.page_size < 1 or args.page_size > 100:
        raise ValueError("--page-size must be between 1 and 100 (HackerOne API hard cap)")
    if args.max_pages < 1:
        raise ValueError("--max-pages must be >= 1")

    parse_interval(args.initial_interval)


def setup_output_directory(output_dir):
    output_dir = os.path.abspath(output_dir)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def setup_logger(output_dir):
    log_path = os.path.join(output_dir, "test-api.log")
    logger = logging.getLogger("hackerone-test-api")
    logger.setLevel(logging.DEBUG)
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger, log_path


def print_banner():
    print("=" * 72, flush=True)
    print("HackerOne — API Connectivity & Flow Test", flush=True)
    print("Endpoint:  GET /v1/reports", flush=True)
    print("Purpose:   Validate auth, pagination, and response shape before CEL build.", flush=True)
    print("=" * 72, flush=True)


def print_parameter_summary(args, logger):
    print("Configuration:", flush=True)
    print("  Base URL              : %s" % args.url, flush=True)
    print("  Token identifier      : %s" % mask_secret(args.api_token_identifier), flush=True)
    print("  Token value           : %s" % mask_secret(args.api_token_value), flush=True)
    print("  Programs              : %s" % (", ".join(args.program) if args.program else "(none)"), flush=True)
    print("  Inbox IDs             : %s" % (", ".join(args.inbox_id) if args.inbox_id else "(none)"), flush=True)
    print("  Initial lookback      : %s" % args.initial_interval, flush=True)
    print("  Page size             : %d" % args.page_size, flush=True)
    print("  Max pages             : %d" % args.max_pages, flush=True)
    if args.state:
        print("  State filter          : %s" % ", ".join(args.state), flush=True)
    if args.severity:
        print("  Severity filter       : %s" % ", ".join(args.severity), flush=True)
    if args.proxy:
        print("  Proxy                 : %s" % args.proxy, flush=True)
    print("  Output directory      : %s" % args.output_dir, flush=True)
    print("  Mode                  : %s" % ("MOCK (no archive)" if args.mock else "ARCHIVE"), flush=True)
    print("", flush=True)
    logger.info("Resolved configuration: url=%s programs=%s inbox_ids=%s "
                "initial_interval=%s page_size=%d max_pages=%d states=%s severities=%s mock=%s",
                args.url, args.program, args.inbox_id, args.initial_interval,
                args.page_size, args.max_pages, args.state, args.severity, args.mock)


def print_summary(success, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, output_dir, archive_path, mock):
    print("", flush=True)
    print("=" * 72, flush=True)
    print("Execution summary", flush=True)
    print("=" * 72, flush=True)
    print("Status               : %s" % ("SUCCESS" if success else "FAILED"), flush=True)
    print("Pages fetched        : %d" % pages_fetched, flush=True)
    print("Total events         : %d" % total_events, flush=True)
    if state_counts:
        rows = ", ".join("%s=%d" % (k, state_counts[k]) for k in sorted(state_counts))
        print("By state             : %s" % rows, flush=True)
    if severity_counts:
        rows = ", ".join("%s=%d" % (k, severity_counts[k]) for k in sorted(severity_counts))
        print("By severity          : %s" % rows, flush=True)
    if cursor_advance:
        print("Highest last_activity_at observed (next cursor): %s" % cursor_advance, flush=True)
    print("Output directory     : %s" % output_dir, flush=True)
    if mock:
        print("", flush=True)
        print("Mock mode: archive step skipped.", flush=True)
        print("All request/response results are logged in the output directory:", flush=True)
        print("  %s/test-api.log   — verbose step-by-step log" % output_dir, flush=True)
        print("  %s/trace.json     — detailed request/response trace" % output_dir, flush=True)
    else:
        if archive_path:
            print("Archive              : %s" % archive_path, flush=True)
            print("", flush=True)
            print("Please send the .tar.gz archive above back to the integration maintainers.", flush=True)
        else:
            print("Archive              : (failed to create — see test-api.log; share the directory directly)", flush=True)


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    print_banner()

    try:
        normalize_args(args)
    except ValueError as exc:
        print("ERROR: %s" % exc, flush=True)
        return 1

    if not args.api_token_identifier or not args.api_token_value:
        print("ERROR: --api-token-identifier and --api-token-value are required "
              "(or HACKERONE_API_TOKEN_IDENTIFIER / HACKERONE_API_TOKEN_VALUE).",
              flush=True)
        return 1
    if not args.program and not args.inbox_id:
        print("ERROR: at least one --program or --inbox-id is required by the HackerOne API.", flush=True)
        return 1

    output_dir = setup_output_directory(args.output_dir)
    args.output_dir = output_dir

    logger, log_path = setup_logger(output_dir)
    sensitive_values = [
        args.api_token_value,
        args.api_token_identifier,
        basic_auth_header(args.api_token_identifier, args.api_token_value),
    ]

    print_parameter_summary(args, logger)

    http = HTTPClient(timeout=args.timeout, proxy_url=args.proxy, logger=logger)

    interrupted = False
    try:
        trace, pages_fetched, total_events, state_counts, severity_counts, cursor_advance, success = collect(
            args, http, logger, sensitive_values
        )
    except KeyboardInterrupt:
        logger.warning("Collection interrupted by user (KeyboardInterrupt)")
        print("\nInterrupted by user.", flush=True)
        trace = []
        pages_fetched = 0
        total_events = 0
        state_counts = {}
        severity_counts = {}
        cursor_advance = None
        success = False
        interrupted = True
    except Exception as exc:
        logger.error("Unhandled error during collection: %s", exc)
        logger.debug("Traceback:\n%s", traceback.format_exc())
        print("ERROR: %s" % exc, flush=True)
        trace = []
        pages_fetched = 0
        total_events = 0
        state_counts = {}
        severity_counts = {}
        cursor_advance = None
        success = False

    try:
        trace_path = write_outputs(output_dir, trace)
        logger.info("Wrote trace to %s", trace_path)
    except Exception as exc:
        logger.error("Failed to write trace.json: %s", exc)
        logger.debug("Traceback:\n%s", traceback.format_exc())

    archive_path = None
    if not args.mock:
        try:
            archive_path = archive_output_dir(output_dir)
            logger.info("Created archive %s", archive_path)
        except Exception as exc:
            logger.error("Failed to create archive: %s", exc)
            logger.debug("Traceback:\n%s", traceback.format_exc())
            archive_path = None

    print_summary(
        success=success,
        pages_fetched=pages_fetched,
        total_events=total_events,
        state_counts=state_counts,
        severity_counts=severity_counts,
        cursor_advance=cursor_advance,
        output_dir=output_dir,
        archive_path=archive_path,
        mock=args.mock,
    )

    return 0 if (success and not interrupted) else 1


if __name__ == "__main__":
    sys.exit(main())
