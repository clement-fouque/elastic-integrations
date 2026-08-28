# GitHub-side operator setup and deployment notes

Operator-facing guide for the custom `elastic_security_advisories` integration: what must be
configured on the GitHub side before the integration will return a single document, and what the
deployment looks like once it does.

Companion documents:

- [`../configuration-plan.md`](../configuration-plan.md) — the configuration variable plan.
- [`github-api-collection-notes.md`](./github-api-collection-notes.md) — API mechanics, endpoint
  choice, incremental-collection strategy, rate-limit reference.
- [`integrations-precedent.md`](./integrations-precedent.md) — reusable patterns from
  `/workspace/packages/`.
- [`esa-publication-landscape.md`](./esa-publication-landscape.md) — advisory volume, cadence, and
  the public fallback data source.

**Verification legend**

- **[VERIFIED-DOC]** — stated in official documentation, link given.
- **[VERIFIED-LIVE]** — reproduced against `api.github.com` / `github.com` during this research on
  2026-08-28. Reproduce with [`../temp/verify-github-setup.sh`](../temp/verify-github-setup.sh).
- **[UNVERIFIED]** — inference or community source only; no official confirmation found.

---

## 1. GitHub-side setup

### 1.0 The short version

| | |
| --- | --- |
| Token type | **Fine-grained personal access token** |
| Resource owner | **`elastic`** — the organization, *not* your user account |
| Repository access | **Only select repositories** → `security-advisories` |
| Permission | **Repository permissions → Contents → Read-only** |
| Also required | **Repository permissions → Metadata → Read-only** — mandatory, granted implicitly |
| Maximum lifetime | 1–366 days, or non-expiring, subject to org policy (default org cap: 366 days) |
| Likely blocker #1 | Organization owner approval, if `elastic` requires it — token is `pending` and reads only public data until approved |
| Likely blocker #2 | The `elastic` organization has SAML SSO configured [VERIFIED-LIVE] |
| Failure signature | **HTTP 404**, not 403 — a broken token is indistinguishable from an empty directory |

### 1.1 Creating a fine-grained PAT scoped to one private organization repository

Official procedure:
<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token>

Steps, with the three that people get wrong called out:

1. Verify your email address on GitHub, if you have not already.
2. Profile picture → **Settings** → **Developer settings** → **Personal access tokens** →
   **Fine-grained tokens** → **Generate new token**.
3. **Token name** — use something that identifies the consumer, e.g.
   `elastic-agent-esa-ingest`.
4. **Expiration** — see §1.4.
5. ⚠️ **Resource owner — this is the step people get wrong.** The selector defaults to *your own
   user account*. You must change it to **`elastic`**. The docs are explicit about what the field
   does:

   > Under Resource owner, select a resource owner. The token will only be able to access
   > resources owned by the selected resource owner. Organizations that you are a member of will
   > not appear if the organization has blocked the use of fine-grained personal access tokens.

   A token whose resource owner is your user account will authenticate successfully, will report
   a valid rate limit, and will return **404** for `elastic/security-advisories`. There is no
   error message that says "wrong resource owner". If `elastic` does not appear in the dropdown at
   all, the organization has disabled fine-grained PATs — see §1.2.
6. **Justification** — if `elastic` requires approval, a free-text justification box appears below
   the resource owner. Fill it in; an organization owner will read it (§1.3).
7. **Repository access** → **Only select repositories** → select `security-advisories`.
   Do not choose "All repositories". Note the docs' caveat that
   *"Tokens always include read-only access to all public repositories on GitHub"* — you cannot
   scope a fine-grained token to *nothing but* one repository; you can only scope its
   **private** access that narrowly.
8. **Permissions** → see §1.5.
9. **Generate token**, then copy the value. It is shown once. It has a `github_pat_` prefix.

Two practical limits from the same page [VERIFIED-DOC]:

- **There is a hard limit of 50 fine-grained PATs per user.**
- Fine-grained tokens *cannot* be created through an API. The web UI is the only path.
  [UNVERIFIED as an official statement — GitHub documents no creation endpoint, and the
  community tracking issue is <https://github.com/orgs/community/discussions/148626>. Treat "no
  API" as true in practice; you cannot automate token minting.]

GitHub does officially support **pre-filling the creation form via URL parameters**, which is the
closest thing to automation available and is worth handing to whoever creates the token
(<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#pre-filling-fine-grained-personal-access-token-details-using-url-parameters>):

```
https://github.com/settings/personal-access-tokens/new
  ?name=elastic-agent-esa-ingest
  &description=Read-only+ingest+of+advisories/+for+the+elastic_security_advisories+integration
  &target_name=elastic
  &expires_in=366
  &contents=read
```

The documented parameters used here are `name`, `description`, `target_name`
("Sets the token's resource target. This is the owner of the repositories that the token will be
able to access. If not provided, defaults to the current user's account"), `expires_in`
("Integer between 1 and 366, or `none` for non-expiring… If not provided, the default is 30 days"),
and `contents=read`. The operator still has to pick the specific repository and click Generate.

Note the docs' own description of that example URL, which is the best official evidence for the
Metadata claim in §1.5:

> Try the URL to create a token with `contents:read` **and `metadata:read`**, with the given name
> and description and an expiration date 45 days in the future.

— the URL specifies only `contents=read`; `metadata:read` is added by GitHub.

### 1.2 The organization must have fine-grained PATs enabled

Organization owners choose, per token type, between "Restrict access via personal access tokens"
and "Allow access via personal access tokens"
(<https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization>)
[VERIFIED-DOC]:

> **Restrict access via personal access tokens:** Personal access tokens (classic) or fine-grained
> personal access tokens cannot access resources owned by the organization. […]
> Regardless of the chosen policy, Personal access tokens will have access to public resources
> within the organization. By default, both Personal access tokens (classic) and fine-grained
> personal access tokens are enabled.

Two consequences worth internalising:

- If `elastic` has restricted fine-grained PATs, **`elastic` will not appear in the Resource owner
  dropdown at all.** That is the diagnostic: an absent org means a policy block, not a membership
  problem.
- "Regardless of the chosen policy, Personal access tokens will have access to public resources."
  This is why a restricted or unapproved token still returns 200 on public endpoints and 404 on
  the private repo — it looks half-working.

Whether the `elastic` organization currently permits fine-grained PATs is **[UNVERIFIED]** — that
setting is not externally observable. Ask an organization owner, or observe whether `elastic`
appears in the dropdown.

### 1.3 Organization owner approval

Default posture, from the same page [VERIFIED-DOC]:

> **Require administrator approval:** An organization owner must approve each fine-grained
> personal access token that can access the organization. Fine-grained personal access tokens
> created by organization owners will not need approval. **This is the default value.**

What that means operationally
(<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>)
[VERIFIED-DOC]:

> If you selected an organization as the resource owner and the organization requires approval for
> fine-grained personal access tokens, then your token will be marked as `pending` until it is
> reviewed by an organization administrator. **Your token will only be able to read public
> resources until it is approved.**

The approval flow, from the organization owner's side
(<https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/managing-requests-for-personal-access-tokens-in-your-organization>)
[VERIFIED-DOC]:

1. GitHub emails organization owners **once daily** with a digest of tokens awaiting approval.
   There is no immediate notification — build this latency into your rollout plan.
2. Owner: Organization → **Settings** → **Personal access tokens** → **Pending requests**.
3. Owner clicks the token, reviews the requested repository access and permissions, then
   **Approve** or **Deny**. A denial can carry a reason, which is emailed to the requester.
4. The requester is emailed on approve or deny.

Approval is **only** a fine-grained-PAT concept:

> Only fine-grained personal access tokens, not personal access tokens (classic), are subject to
> approval. Unless the organization has restricted access by personal access tokens (classic), any
> personal access token (classic) can access organization resources without prior approval.

This asymmetry is a trap: it means the "worse" credential (a classic `repo` token) is the *easier*
one to get working, which pushes tired operators toward the over-privileged option. Resist it.

Ongoing governance: organization owners can list and revoke fine-grained tokens at
Organization → Settings → Personal access tokens → **Active tokens**, individually or in bulk,
and the token owner is emailed on revocation
(<https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/reviewing-and-revoking-personal-access-tokens-in-your-organization>).
**Plan for the possibility that a periodic org-wide token cleanup silently kills this
integration** — the symptom will be a 404, per §1.7.

### 1.4 Token lifetime

| Question | Answer | Source |
| --- | --- | --- |
| Range selectable at creation | **1–366 days**, or non-expiring | `expires_in`: "Integer between 1 and 366, or `none` for non-expiring" [VERIFIED-DOC] |
| Default if unspecified | **30 days**, "or less if the target has a token lifetime policy set" | [VERIFIED-DOC] |
| Is "no expiration" permitted? | **Yes, at the GitHub product level** — "Infinite lifetimes are allowed **but may be blocked by a maximum lifetime policy** set by your organization or enterprise owner" | [VERIFIED-DOC] |
| Organization maximum-lifetime default | For fine-grained PATs, **the default org maximum lifetime policy is 366 days** | [VERIFIED-DOC] |
| Classic PAT lifetime | No expiration requirement at all; but "GitHub automatically removes personal access tokens that haven't been used in a year" | [VERIFIED-DOC] |

Sources:
<https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization#enforcing-a-maximum-lifetime-policy-for-personal-access-tokens>
and the PAT management page linked in §1.1.

Two operational notes:

- **Do not assume "no expiration" will work for `elastic`.** The organization default caps
  fine-grained tokens at 366 days, and an enterprise policy can be stricter. Plan on a **366-day
  maximum** and treat anything longer as a bonus.
- **A non-compliant token is not revoked, it is silently rejected.** From the same page:
  *"When you set a policy, tokens with non-compliant lifetimes will be blocked from accessing your
  organization if the token belongs to a member of your organization. Setting this policy does not
  revoke or disable these tokens. Users will learn that their existing token is non-compliant when
  API calls for your organization are rejected."* If an org owner tightens the lifetime policy
  after you deploy, your working integration starts 404ing with no other signal.

**Rotation is therefore mandatory, not optional.** Set a calendar reminder at expiry minus two
weeks. There is no GitHub-side renewal that preserves the token value; rotation means minting a
new token and updating the integration's `api_key` in Fleet.

### 1.5 The exact permission required

Set exactly one permission, named precisely as it appears in the GitHub UI:

> **Repository permissions → Contents → Read-only**

(API identifier `contents`, access level `read`.)

**[VERIFIED-LIVE]** GitHub tells you this itself. Both endpoints this integration uses return an
`X-Accepted-GitHub-Permissions` response header naming the permission they check:

```
GET /repos/elastic/integrations/git/trees/main:packages%2Fgithub%2Fdata_stream%2Fsecurity_advisories?recursive=1
  HTTP/2 200
  x-accepted-github-permissions: contents=read

GET /repos/elastic/integrations/git/blobs/<sha>
  HTTP/2 200
  x-accepted-github-permissions: contents=read
```

That header is documented as a first-class diagnostic
(<https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api#resource-not-accessible>)
[VERIFIED-DOC]:

> You can use the `X-Accepted-GitHub-Permissions` header to identify the permissions that are
> required to access the REST API endpoint. […] `X-Accepted-GitHub-Permissions: contents=read`
> means that your GitHub App or fine-grained personal access token needs read access to the
> contents permission.

**Also required, and granted automatically:**

> **Repository permissions → Metadata → Read-only** (API identifier `metadata`, access level `read`)

Metadata is mandatory on every fine-grained token and is added implicitly; there is nothing to
click. Evidence:

- The official URL-template example specifies only `contents=read` yet the docs describe the
  result as *"a token with `contents:read` **and `metadata:read`**"* [VERIFIED-DOC].
- The repository-permissions table lists `metadata` with the single access level `read` — there is
  no write variant and no "none" [VERIFIED-DOC].
- **[VERIFIED-LIVE]** `GET /repos/{owner}/{repo}` returns
  `x-accepted-github-permissions: metadata=read`. Every REST call that resolves an
  `{owner}/{repo}` pair transits that check.
- The characterisation "mandatory and granted automatically" is **[UNVERIFIED]** as a single
  quotable sentence in GitHub's own docs — the three points above are indirect but mutually
  consistent, and it is universally reported by third parties. Practically: do not try to enable
  it, and do not add `metadata=read` to a pre-fill URL.

**Do not grant anything else.** In particular do not grant `Contents: Read and write`, and do not
grant the tempting-sounding **Repository permissions → "Repository security advisories"**
(`repository_advisories`) — that permission governs GitHub-*native* advisory objects in a repo's
Security tab, which are a completely different entity from files in an `advisories/` directory
(see `integrations-precedent.md` §5.2).

### 1.6 SAML SSO and SCIM

**The `elastic` organization has SAML single sign-on configured.** [VERIFIED-LIVE] —
`https://github.com/orgs/elastic/sso` returns HTTP 200 and renders
*"Single sign-on to elastic — Authenticate your account by logging into elastic's single sign-on
provider"*, whereas the same path on organizations with no SAML configuration
(`google`, `jquery`, `expressjs`, `octokit`, `nodejs`) returns **404**. Whether SSO is merely
*enabled* or fully *enforced* for all members is **[UNVERIFIED]** — that distinction is not
externally observable, and the docs describe them as separate settings
(<https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enforcing-saml-single-sign-on-for-your-organization>).

The critical difference between the two token types
(<https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on>)
[VERIFIED-DOC]:

> You must authorize your personal access token (classic) after creation before the token can
> access an organization that uses SAML single sign-on (SSO). […] **Fine-grained personal access
> tokens are authorized during token creation, before access to the organization is granted.**

So:

- **Classic PAT** — after creating it you must go to Settings → Developer settings → Personal
  access tokens, find the token, click **Configure SSO**, and click **Authorize** next to
  `elastic`. Miss this step and the token returns **404** on the private repo while working
  perfectly against public endpoints. This is the single most common "my token is valid but
  everything 404s" cause. The docs also note: *"If you don't see Configure SSO, ensure that you
  have authenticated at least once through your identity provider."*
- **Fine-grained PAT** — there is **no separate Configure SSO step**; SSO authorization happens
  implicitly when you select `elastic` as the Resource owner. This is a real advantage of the
  fine-grained token and another reason to prefer it.

Prerequisite for either: **you must have a linked external identity** in the organization, created
by authenticating to `elastic` through its IdP at least once in a browser
(<https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/about-authentication-with-single-sign-on>):

> Before you can authorize a personal access token or SSH key, you must have a linked external
> identity. If you're a member of an organization where SSO is enabled, you can create a linked
> external identity by authenticating to your organization with your identity provider (IdP) at
> least once.

And note this gotcha, which bites service accounts specifically:

> If you have a linked identity for an organization, you can only use **authorized** personal
> access tokens and SSH keys with that organization, **even if SSO is not enforced.**

Once authorized, the token stays authorized until one of the following, all of which will break
ingestion silently with a 404 [VERIFIED-DOC]:

- an organization or enterprise owner revokes the authorization;
- **you are removed from the organization** — this is the leaver risk (a fine-grained token "will
  become inactive if the user loses access to the resource");
- the scopes on a classic PAT are edited, or the token is regenerated;
- the token expires.

**SCIM.** SCIM provisions and de-provisions GitHub org membership from the IdP. It does not add a
separate token-authorization step. Its relevance here is entirely about durability: if `elastic`
uses SCIM, then de-provisioning the token owner in the IdP removes them from the organization,
which inactivates the token. That makes **"who owns this token" a real operational decision** — a
personal token belonging to an individual engineer is a single point of failure tied to that
person's employment.

Two mitigations, in order:

1. **A machine/service GitHub account** that is a member of `elastic` with an IdP identity and
   read access to `security-advisories`. GitHub documents this pattern for SAML orgs at
   <https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/managing-bots-and-service-accounts-with-saml-single-sign-on>.
   Whether `elastic` policy permits such accounts is **[UNVERIFIED]**.
2. Failing that, document the token owner in the runbook and treat their departure as a
   scheduled outage.

A GitHub App would sidestep all of this, and it is the option GitHub itself recommends
(*"To access resources on behalf of an organization, or for long-lived integrations, you should use
a GitHub App"*). It is **not available to us**: minting an installation token requires signing an
RS256 JWT, and mito's CEL crypto library exposes only HMAC — no RSA, no JWT builder. See
`github-api-collection-notes.md` §4.3 for the verified detail. This is worth stating in the design
doc, because it is the first question a reviewer will ask.

### 1.7 The classic-PAT alternative, and why not to use it

| | Fine-grained PAT | Classic PAT |
| --- | --- | --- |
| Scope needed | `Contents: Read-only` on **one** repository | **`repo`** |
| What that grants | Read the contents of `elastic/security-advisories` | See below |
| SSO | Authorized at creation | Separate **Configure SSO → Authorize** step, easy to miss |
| Org approval | May be required (default: yes) | Never required |
| Lifetime | 1–366 days or infinite, org-capped (default cap 366d) | Optional expiry, may be unlimited |
| Verdict | ★ **Use this** | Fallback only |

There is **no read-only classic scope for private repository contents**. The narrowest classic
scope that works is `repo`, described verbatim as
(<https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps>)
[VERIFIED-DOC]:

> `repo` — Grants full access to public and private repositories including **read and write access
> to code**, commit statuses, repository invitations, collaborators, deployment statuses, and
> repository webhooks. Note: In addition to repository related resources, the `repo` scope also
> grants access to manage organization-owned resources including projects, invitations, team
> memberships and webhooks. This scope also grants the ability to manage projects owned by users.

Combined with:

> If you choose to use a personal access token (classic), keep in mind that it will grant access to
> **all repositories within the organizations that you have access to**, as well as all personal
> repositories in your personal account.

The blast radius, concretely: a credential sitting in an Elastic Agent policy to read ~300 Markdown
files would also be able to **push code to every repository in every Elastic organization the
owner can reach**, manage team memberships, and create webhooks. For an owner with broad `elastic`
access that is close to unlimited write authority over Elastic's source code. It also cannot be
scoped down — `repo` has no read-only variant and no per-repository restriction.

Use it only if fine-grained PATs are blocked at the org level (§1.2) *and* an exception is
impossible. If you must:

- Grant `repo` and nothing else — **not** `admin:org`, `workflow`, or `delete_repo`.
- Set the shortest workable expiry.
- **Do the Configure SSO → Authorize step for `elastic`** (§1.6).
- Own it from a dedicated service account, never a human's primary account.
- Note that an org can disable classic PATs entirely, in which case *"your request will fail with a
  `403` response"* [VERIFIED-DOC] — a rare case where GitHub gives you a 403 rather than a 404.

### 1.8 Verifying the 404-not-403 failure mode, and how to self-diagnose it

**Confirmed.** GitHub states it plainly
(<https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api#404-not-found-for-an-existing-resource>)
[VERIFIED-DOC]:

> If you make a request to access a private resource and your request isn't properly authenticated,
> you will receive a `404 Not Found` response. GitHub uses a `404 Not Found` response **instead of
> a `403 Forbidden` response to avoid confirming the existence of private repositories**.

**[VERIFIED-LIVE]** the responses are not merely both 404 — they are byte-identical **for a given
endpoint**. Re-verified on the review pass: md5 `a11f74e873af40b9e9ea935139d48c61` across five
variants of the same endpoint. The one qualification worth stating precisely, because the original
wording overreached: the bodies differ **between** endpoints, since `documentation_url` names the
endpoint that was called. That is enough to tell you *which call* failed but nothing about *why*, so
the diagnostic problem below is unchanged.

```
$ curl -H "Authorization: Bearer <token-without-access>" \
       https://api.github.com/repos/elastic/security-advisories
HTTP/2 404
x-accepted-github-permissions: metadata=read
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/repos/repos#get-a-repository","status":"404"}

$ curl -H "Authorization: Bearer <same-token>" \
       https://api.github.com/repos/elastic/this-repo-does-not-exist-zzz9
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/repos/repos#get-a-repository","status":"404"}

$ curl https://api.github.com/repos/elastic/security-advisories     # no Authorization at all
{"message":"Not Found","documentation_url":"...","status":"404"}
```

Worse, on the endpoints this integration actually calls, **four distinct faults all produce the
same 404** [VERIFIED-LIVE]:

| Fault | Response |
| --- | --- |
| Token lacks access to the repository | `404 {"message":"Not Found", …/git/trees#get-a-tree}` |
| Repository does not exist / name typo | `404`, same body |
| `path` (directory) does not exist in the repo | `404`, same body |
| `branch` / ref does not exist | `404`, same body |
| **`path` points at a file rather than a directory** | **HTTP 422**, distinct message — the one input error that *is* distinguishable |

So "no data is arriving" gives the operator essentially no information, with the single exception of
the 422 case. The diagnosis has to be done by hand, from the outside in.

> **Correction (review pass 2) — the ladder below cannot do everything it claims.** Step 3a tells the
> operator that a 404 on the repository-root tree means the `Contents: Read` permission is missing. It
> does not: a nonexistent branch produces the identical 404 at that same step, so 3a cannot separate
> the two faults it purports to separate. **Read 3a as "either the permission is missing or the branch
> name is wrong"**, and disambiguate by requesting the tree by the *default* branch name returned from
> the repository probe in step 2, or by commit SHA. Only if that also 404s is the permission genuinely
> the problem. The rest of the ladder is sound.

#### The diagnostic ladder

Run these in order from a host with the same network path as the agent. Stop at the first failure;
that step names the fault. Substitute the real token for `$TOKEN`.

```bash
TOKEN='github_pat_...'
H=(-H "Accept: application/vnd.github+json" \
   -H "X-GitHub-Api-Version: 2022-11-28" \
   -H "Authorization: Bearer $TOKEN")

# STEP 1 — Is the token syntactically valid and is the API reachable at all?
curl -sS -D- -o /dev/null "${H[@]}" https://api.github.com/rate_limit
```

*Working:* `HTTP/2 200` with `x-ratelimit-limit: 5000`.
*Broken:* `HTTP/2 401 {"message":"Bad credentials"}` — the token string is wrong, truncated, or
revoked. `x-ratelimit-limit: 60` means the `Authorization` header is not being sent or is being
stripped (check for a TLS-intercepting proxy).

```bash
# STEP 2 — Can the token see the repository at all? This is the decisive test.
curl -sS -D- "${H[@]}" https://api.github.com/repos/elastic/security-advisories
```

*Working* — HTTP 200 and a body containing:

```json
{
  "full_name": "elastic/security-advisories",
  "private": true,
  "visibility": "private",
  "default_branch": "main"
}
```

Note `default_branch`: **this is where you confirm the value for the integration's `branch`
variable** rather than assuming `main`.

*Broken* — `HTTP/2 404` with `x-accepted-github-permissions: metadata=read`. Work through, in
order of likelihood:

1. **Resource owner is your user account, not `elastic`.** Open the token at
   Settings → Developer settings → Fine-grained tokens and read the owner shown at the top.
   This is the most common cause and cannot be fixed by editing — mint a new token.
2. **The token is `pending` organization approval.** The same token page shows the pending state.
   Chase an `elastic` organization owner (§1.3); remember the notification email is a daily digest.
3. **Classic PAT not SSO-authorized.** Settings → Developer settings → Tokens (classic) →
   **Configure SSO** → **Authorize** next to `elastic` (§1.6).
4. **The repository is not in the token's selected-repositories list.** Fine-grained tokens
   default to "Public repositories only".
5. **The token's owner does not have read access to the repository.** A token cannot exceed its
   owner's own access: *"A token has the same capabilities to access resources and perform actions
   on those resources that the owner of the token has"* [VERIFIED-DOC]. Have the owner open
   <https://github.com/elastic/security-advisories> in a browser. If *they* get a 404, the problem
   is repository access, not the token — request access first.
6. **The org revoked the token, or a lifetime policy now rejects it** (§1.3, §1.4).

```bash
# STEP 3 — Can the token read the advisories/ tree? Confirms Contents:Read.
curl -sS -D- -o /tmp/tree.json "${H[@]}" \
  "https://api.github.com/repos/elastic/security-advisories/git/trees/main:advisories?recursive=1"
python3 -c "import json;d=json.load(open('/tmp/tree.json'));print(len(d['tree']),'entries; truncated =',d['truncated'])"
```

*Working:* `HTTP/2 200`, an `etag:` header, `x-accepted-github-permissions: contents=read`, and a
non-zero entry count with `truncated = False`.
*Broken with 200 but 0 entries:* the directory genuinely is empty, or `path` is wrong in a way that
still resolves (e.g. it names a file, not a directory).
*Broken with 404, given Step 2 passed:* the repository is reachable, so the fault is now narrowed
to exactly three things — the **permission** is not `Contents: Read-only`, the **branch** does not
exist, or the **directory path** does not exist. Distinguish them:

```bash
# 3a. Is Contents:Read actually granted?  Read the repo root tree.
curl -sS -o /dev/null -w 'root tree: %{http_code}\n' "${H[@]}" \
  "https://api.github.com/repos/elastic/security-advisories/git/trees/main"
#     404 here, with Step 2 passing => the permission is missing. Re-mint with Contents: Read-only.
#     200 here => permission is fine; the branch and directory are the remaining suspects.

# 3b. Does the branch exist?  (Compare against default_branch from Step 2.)
curl -sS "${H[@]}" \
  "https://api.github.com/repos/elastic/security-advisories/branches" \
  | python3 -c "import json,sys;print([b['name'] for b in json.load(sys.stdin)])"

# 3c. Does the directory exist, and what is actually in it?
curl -sS "${H[@]}" \
  "https://api.github.com/repos/elastic/security-advisories/git/trees/main" \
  | python3 -c "import json,sys;print([(t['path'],t['type']) for t in json.load(sys.stdin)['tree']])"
```

```bash
# STEP 4 — Can the token read one blob? Confirms the full read path end to end.
SHA=$(python3 -c "import json;d=json.load(open('/tmp/tree.json'));print([t['sha'] for t in d['tree'] if t['type']=='blob'][0])")
curl -sS -D- -o /dev/null "${H[@]}" \
  "https://api.github.com/repos/elastic/security-advisories/git/blobs/$SHA"
```

*Working:* `HTTP/2 200`, `x-accepted-github-permissions: contents=read`, and an `etag:` header.

If Steps 1–4 all pass and the integration still produces nothing, the fault is in the integration
configuration (`api_url`, `owner`, `repo`, `path`, `branch`, or a `file_pattern` that matches
nothing) or in the agent's network path — not on the GitHub side.

#### What the integration should surface

`integrations-precedent.md` §10 gives the standard CEL error-event shape. The one addition this
data source needs is that a **404 on the tree request must not be reported as "no data"** — it
should produce an error message that names the likely cause. Otherwise the most common
misconfiguration in this integration presents to the user as a healthy, empty data stream. (The
exact wording is a decision for whoever writes the CEL program; the requirement is recorded here.)

---

## 2. Deployment notes

### 2.1 Network requirements

| Direction | Destination | Port | Protocol | Required? |
| --- | --- | --- | --- | --- |
| Outbound | `api.github.com` | 443 | HTTPS / TLS 1.2+ | **Yes** (github.com deployments) |
| Outbound | GHES host, e.g. `ghes.example.com` | 443 | HTTPS | Only for GitHub Enterprise Server |
| Outbound | GHEC data-residency host, e.g. `api.SUBDOMAIN.ghe.com` | 443 | HTTPS | Only for GHEC with data residency |
| Outbound | DNS resolver | 53 | UDP/TCP | Yes |
| Inbound | — | — | — | **None.** This is a pull-only integration; no listener, no ingress, no public endpoint. |

Only `api.github.com` is needed. The design deliberately avoids `raw.githubusercontent.com`
(`github-api-collection-notes.md` §1.5) — a secondary benefit of that choice is that it keeps the
egress allow-list to a single hostname. Git protocol access (port 22 / `git://`) is not used, so
the `git` IP ranges and `codeload.github.com` are irrelevant here.

**IP allow-listing.** If the agent's network requires destination IPs rather than hostnames, the
authoritative source is `GET https://api.github.com/meta` — **the relevant key is `api`**
(<https://docs.github.com/en/rest/meta/meta#get-github-meta-information>). [VERIFIED-LIVE] it
currently returns **26 CIDR blocks** (IPv4 and IPv6) under that key:

```
192.30.252.0/22   185.199.108.0/22   140.82.112.0/20   143.55.64.0/20
2a0a:a440::/29    2606:50c0::/32
20.201.28.148/32  20.205.243.168/32  20.87.245.6/32    4.237.22.34/32
4.228.31.149/32   20.207.73.85/32    20.27.177.116/32  20.200.245.245/32
20.175.192.149/32 20.233.83.146/32   20.29.134.17/32   20.199.39.228/32
20.217.135.0/32   4.225.11.201/32    4.208.26.200/32   20.26.156.210/32
172.182.252.137/32 4.249.131.166/32  48.202.248.39/32  48.204.201.2/32
```

Do **not** hardcode that list. GitHub's own guidance
(<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses>)
[VERIFIED-DOC]:

> The list of GitHub IP addresses returned by the Meta API is **not intended to be an exhaustive
> list**. […] We make changes to our IP addresses from time to time. **We do not recommend allowing
> by IP address**, but if you use these IP ranges we strongly encourage regular monitoring of our
> API.
>
> For applications to function, you must allow TCP ports 22, 80, and 443 via our IP ranges for
> `github.com` and `SUBDOMAIN.ghe.com`.

Recommendation: allow-list by **hostname** (`api.github.com`) at an egress proxy if at all
possible. If IP allow-listing is mandatory, automate a periodic refresh from the `api` key and
alert on drift; a stale list will present as a connection timeout, which at least fails more
loudly than the 404 class of failure. The `api` list has grown steadily and includes IPv6 — a
v4-only allow-list will work today but is fragile.

**TLS.** `api.github.com` uses a public CA chain; no `ssl` configuration is needed. Two cases do
need it: a GHES instance with a private/internal CA, and a TLS-intercepting corporate proxy. Both
are handled by the `ssl` variable (see the configuration plan).

### 2.2 Proxy support

Two mechanisms, in precedence order:

1. **The `proxy_url` variable** maps to the CEL input's `resource.proxy_url` option
   (<https://www.elastic.co/docs/reference/beats/filebeat/filebeat-input-cel>), in the form
   `http[s]://<user>:<password>@<host>:<port>`. Username and password must be **URL-encoded** —
   this is the wording the `github` package already uses and it is worth keeping verbatim, because
   an unencoded `@` or `:` in a password is a recurring support issue.
2. **Environment variables** — `HTTPS_PROXY` / `HTTP_PROXY` / `NO_PROXY` in the Elastic Agent
   process environment are honoured by Go's default HTTP transport. `resource.proxy_url` overrides
   them for this input.

Notes:

- A proxy that terminates TLS will present its own certificate; configure the `ssl` variable's
  `certificate_authorities` with the proxy's CA, or the agent will fail the handshake.
- **`proxy_url` is not marked `secret: true`** anywhere in the monorepo, including the `github`
  package. If the proxy requires credentials, they will be stored in the Fleet policy in the clear.
  Prefer a proxy that authenticates by source IP, or an unauthenticated egress proxy in front of a
  firewall rule. This is a residual risk to note in the integration README rather than something to
  fix with a new variable.
- **Agentless deployments have no proxy.** The agentless runner reaches `api.github.com` directly
  over the internet; `proxy_url` is meaningless there.

### 2.3 Where the agent should run, and the multi-agent duplication problem

**This should be treated as a single-agent integration.** The reason is structural, not a
preference:

The CEL input persists its incremental state (`state.cursor` — the sub-tree ETag and the
`path → blob SHA` map) in the **local Filebeat registry on the agent host**. There is no shared or
centralised cursor. So if an Elastic Agent *policy* containing this integration is applied to N
agents, you get **N wholly independent collectors**, each with its own cursor, each enumerating the
same directory and fetching the same blobs. That is:

- **N× the documents.** Every advisory is indexed N times.
- **N× the API cost**, all charged to the same token and — critically — the same **per-user**
  5,000/hr bucket (§2.4).
- **N× the backfill.** With N=10 and a 500-file corpus that is 5,010 requests, which exceeds the
  entire hourly budget on day one.
- **Divergent state.** Agents added later backfill from scratch while existing agents are in steady
  state, so the duplicate count is not even stable.

Fleet does **not** enforce singleton integrations. There is no `max_agents: 1` in the package spec.
So this has to be handled by deployment discipline, and it should be called out prominently in the
integration README.

Recommended approach, in order of preference:

1. **Agentless (Elastic Cloud).** Elastic runs exactly one managed collector for the integration
   policy; there is no agent for a user to accidentally enrol twice. This is the cleanest answer
   and it has direct precedent — the `github` package enables agentless on its policy template
   (`packages/github/manifest.yml:53-61`). Constraints: the runner needs plain internet egress to
   `api.github.com` (it has it), `proxy_url` and host-local file paths are unavailable, and the
   request tracer writes to a filesystem you cannot easily reach. Suitable here because the data
   source is a public-internet SaaS API and the integration needs nothing host-local.
2. **A dedicated single-agent policy.** Create an agent policy whose *only* integration is
   `elastic_security_advisories`, and enrol exactly one agent in it. Do not add this integration to
   a shared policy that many agents run. Document this in the README as a hard requirement, and
   name the failure mode explicitly ("adding this to a multi-agent policy will duplicate every
   advisory N times") — operators will otherwise reasonably assume Fleet handles it.
3. **Deterministic document `_id`.** Fingerprinting the document `_id` from a stable key (the ESA
   identifier, or the file path plus blob SHA) makes duplicate ingestion **idempotent**: N agents
   writing the same advisory produce one document, not N. This does not reduce API cost, and it
   does not fix the divergent-backfill problem, but it converts a data-correctness bug into a mere
   efficiency loss — which is a very good trade for an accident you cannot prevent. This is a
   pipeline design decision and belongs to the ingest-pipeline/field-mapping work, not to this
   configuration plan; it is flagged here as a requirement to hand over.

Host placement, if running a self-managed agent: anywhere with outbound 443 to `api.github.com`.
There is no locality requirement, no on-host data source, and negligible CPU/memory/disk footprint.
Pick a host with stable uptime, because a long outage lengthens detection latency (though it costs
nothing — the ETag strategy resynchronises on the next successful poll and the blob-SHA map
compares *state*, not history, so there is no backlog to replay and no "missed window").

**High availability is deliberately not recommended.** Running two agents for redundancy is exactly
the duplication scenario above. Advisory data is not real-time-critical at minute granularity;
accept single-collector operation and monitor for collection failure instead.

### 2.4 Rate-limit budget in practice

Budget: **5,000 requests/hour**, verified live for both fine-grained and classic PATs
(`github-api-collection-notes.md` §3.2).

With `interval: 1h` and the recommended sub-tree-ETag strategy (Strategy A):

| Scenario | Requests issued | Rate-limit units consumed | % of one hour's budget |
| --- | --- | --- | --- |
| Poll, nothing changed (the overwhelmingly common case) | 1 conditional `GET` → **304** | **0** | **0 %** |
| Full quiet day (24 polls, no changes) | 24 | **0** | **0 %** |
| Poll on a typical publication day (~11 files) | 1 tree + 11 blobs | 12 | 0.24 % |
| Poll on the largest observed batch (48 advisories, 2026-08-13) | 1 tree + 48 blobs | 49 | **0.98 %** |
| Initial backfill, 200-file corpus | 1 tree + 200 blobs | 201 | 4.0 % |
| Initial backfill, 500-file corpus | 1 tree + 500 blobs | 501 | 10.0 % |
| **Typical month** (≈720 polls, ~1.2 batches) | ~740 | **< 100** | < 0.003 % of the monthly 3.65 M |

The 304-is-free property is the load-bearing fact, and it is conditional
(<https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#use-conditional-requests>)
[VERIFIED-DOC, and VERIFIED-LIVE in `github-api-collection-notes.md` §3.1]:

> Making a conditional request does not count against your primary rate limit if a `304` response
> is returned **and the request was made while correctly authorized with an `Authorization`
> header**.

An *unauthenticated* 304 does consume budget — irrelevant here, since the token is mandatory, but
it means a configuration that accidentally drops the `Authorization` header degrades from
0 units/day to 24, and simultaneously drops the ceiling from 5,000/hr to 60/hr.

Secondary limits are not a concern at this volume: the ceiling is **900 points/min against a single
REST endpoint**, and a `GET` costs 1 point. A 500-blob backfill issued serially at ~250 ms per
request runs at ~240 requests/min against the Blobs endpoint — under 30 % of the cap. GitHub
explicitly advises issuing requests **serially rather than concurrently**; following that advice
keeps this comfortably safe. Do not parallelise the blob fetches to speed up backfill; there is no
need, and it is the one way to trip a secondary limit here.

**Interaction with the existing `github` package — this is the one real risk.**

The 5,000/hour primary limit is **per user, not per token**
(<https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#primary-rate-limit-for-authenticated-users>)
[VERIFIED-DOC]:

> You can use a personal access token to make API requests. Additionally, you can authorize a
> GitHub App or OAuth app, which can then make API requests on your behalf. **All of these requests
> count towards your personal rate limit of 5,000 requests per hour.**

So **minting a second token does not buy a second budget** if both tokens belong to the same GitHub
user. This is counterintuitive and is the thing to get right.

Now consider the `github` package's own `security_advisories` CEL stream. It targets
`https://api.github.com/advisories` — the *global* GitHub Advisory Database — walks it with
`per_page=100` via `Link: rel="next"`, and sets `max_executions: 5000`
(`integrations-precedent.md` §4, §5.1). A single poll can therefore issue **up to 5,000
requests — the entire personal hourly budget — on its own.** (The exact number depends on the
corpus size, which is **[UNVERIFIED]**; the reviewed advisory database is large enough that
`max_executions` is the binding constraint, not exhaustion of the feed.) Its default interval is
`24h`, so this is a once-a-day spike rather than sustained pressure, but the spike is total.

Consequences and mitigations:

| Situation | Outcome |
| --- | --- |
| Same GitHub user owns the token for both integrations | The `github` package's advisory sweep can exhaust the shared 5,000/hr. This integration then gets 403/429 on its tree request for the remainder of that hour. |
| Different GitHub users (e.g. a dedicated service account for this integration) | Fully independent 5,000/hr buckets. **This is the fix.** |
| Only this integration | Effectively zero consumption; the budget is a non-issue. |

Recommendation: **own this integration's token from a GitHub account that is not also running the
`github` package.** If that is impossible, the damage is bounded and self-healing — on a 403/429
the integration must back off *without advancing its cursor* (`integrations-precedent.md` §8), so
the only cost is detection latency, not lost advisories. Note also that GitHub returns **403 or 429
for both primary and secondary limits**, and (verified live in `github-api-collection-notes.md`
§3.5) can return 429 while `x-ratelimit-remaining` is still non-zero — so the status code must be
treated as authoritative on its own.

**GHES note.** GitHub Enterprise Server administrators configure rate limiting separately, and it
is **disabled by default** on GHES. The figures above are for github.com. [UNVERIFIED for any
specific GHES deployment — ask its administrator.]

### 2.5 Data volume estimate

Grounding figures from `esa-publication-landscape.md` §1.3 and §2.2: 203 ESA-tagged Discourse
topics; 40 advisories in ESA-year 2024, 36 in 2025, **116 in 2026 through 2026-08-28**; 52 distinct
publication dates across the corpus; largest single-day batch **48** (2026-08-13); 340
Elastic-assigned CVE records; 244 records in the community scrape.

| Metric | Estimate | Basis |
| --- | --- | --- |
| Documents on initial backfill | **≈ 200–500** | One document per file. 203 published ESAs is a floor; ESA IDs are reserved-then-published with gaps, so the repo may hold unpublished drafts too. 340 CVE records and the prior track's 200–500 working assumption bracket the upper end. **[UNVERIFIED]** — the directory is unreadable; see `esa-publication-landscape.md` §5.1. |
| New documents per month, 2026 run-rate | **≈ 15** | 116 advisories in ~7.9 months = 14.7/month. |
| New documents per month, 2024–25 rate | **≈ 3** | 40 and 36 per year. Volume grew ~3× into 2026; plan for the 2026 rate. |
| Documents on a typical publication day | **6–19** | Observed batch sizes: 48, 19, 11, 10, 6, 6, 7, 7, 11. Median ≈ 10. |
| Worst-case single poll | **48** | The 2026-08-13 batch. Design headroom for ~100. |
| Document writes per month incl. edits | ≈ 15–30 | An edit to an existing advisory changes its blob SHA and triggers a re-fetch and re-index. Edit rate is **[UNVERIFIED]**. |
| Approximate index size, full corpus | **≈ 2–10 MB** | 500 documents × ~4–20 KB of advisory text plus ECS fields. A worked ESA example is ~3 KB of Markdown (`esa-publication-landscape.md` §3.4). |
| Monthly index growth | **well under 1 MB** | |

**This is a very small data stream.** Nothing about it needs ILM tuning, shard planning, or
capacity review; the entire historical corpus is smaller than a single second of a typical firewall
log stream. Plan the index for queryability and retention-forever, not for volume.

### 2.6 Initial backfill behaviour and duration

On the first run the cursor is empty, so there is no stored ETag and no `path → blob SHA` map. The
integration therefore:

1. Issues an unconditional `GET` of the `advisories/` sub-tree — 1 request, returns every file's
   path, size, and blob SHA, and an `etag` to store.
2. Fetches every blob — N requests, one per file.
3. Stores the ETag and the full `path → blob SHA` map in `state.cursor`.

From then on, the steady state described in §2.4 applies. There is no time-window replay, no
`initial_interval` to configure, and no risk of a partial-history gap: the first poll captures the
complete current state of the directory by construction.

**Duration.** 201–501 serial HTTPS requests. At an observed ~150–400 ms per request against
`api.github.com`:

| Corpus | Requests | Wall clock (serial) |
| --- | --- | --- |
| 200 files | 201 | **≈ 30 s – 1.5 min** |
| 350 files | 351 | ≈ 1 – 2.5 min |
| 500 files | 501 | **≈ 1.5 – 3.5 min** |

**Rate limits do not constrain the backfill.** 501 requests is 10 % of a single hour's budget, and
at ~240 requests/min it stays well under the 900 points/min secondary limit. The backfill completes
inside one poll interval at any recommended interval value, and inside the first rate-limit window
regardless.

Three operational caveats:

- **CEL execution budget.** `max_executions` defaults to **1,000** and bounds how many times the
  program may re-run via `want_more`. A backfill that fetches one blob per execution needs ~N+1
  executions, so a 500-file corpus leaves only 2× headroom, and exceeding the budget stops
  processing and logs a warning until the next interval. The `github` package raises this to
  `max_executions: 5000` (`integrations-precedent.md` §4) and this integration should do the same.
  That is a template constant, not a user-facing variable — recorded here as a handover note.
- **Backfill is resumable but not incremental within a poll.** If the agent restarts mid-backfill
  before the cursor is written, the next poll starts over. That costs another ≤501 requests, which
  is affordable, but it means "restart the agent repeatedly during setup" is the one way to burn
  budget. Let a backfill finish.
- **Tree truncation.** The Trees API sets `"truncated": true` past 100,000 entries. At 200–500
  files this cannot be hit, but the flag must be checked rather than assumed — silent truncation is
  exactly the failure the Contents API exhibits and the reason the Trees API was chosen
  (`github-api-collection-notes.md` §1.2).

### 2.7 Post-deployment verification checklist

1. **Documents arrived.** Query the data stream; expect a count in the low hundreds within ~5
   minutes of enabling the integration. A count of exactly **0** with no errors is the 404
   signature — go to §1.8.
2. **Advisory identifiers look right.** Spot-check that documents carry plausible `ESA-YYYY-NN`
   identifiers spanning multiple years, not just recent ones. A recent-only corpus suggests the
   directory is year-nested and `path` is pointing at one year.
3. **The second poll is a 304.** In the agent logs (or via the request tracer) confirm the second
   interval's tree request returns 304 and produces no events. If every poll re-fetches every blob,
   the ETag is not being stored or echoed correctly — the cost jumps from 0 to ~500 units/hour.
4. **Rate limit is healthy.** `GET /rate_limit` with the same token should show `core.used` in the
   low hundreds after backfill and essentially flat thereafter.
5. **Only one agent is collecting.** In Fleet, confirm the integration's policy has exactly one
   enrolled agent (§2.3). Verify no duplicate documents per advisory identifier.
6. **Token expiry is on the calendar.** Record the expiry date and set a reminder at expiry minus
   two weeks (§1.4). Expiry presents as a 404, not an auth error.

---

## 3. Gaps and open questions

1. **Whether the `elastic` organization permits fine-grained PATs, and whether it requires owner
   approval.** [UNVERIFIED] — neither setting is externally observable. Both are on the critical
   path; confirm with an organization owner before committing to a rollout date.
2. **Whether the `elastic` organization enforces (as opposed to merely enables) SAML SSO, and
   whether it uses SCIM.** [UNVERIFIED]. SSO is definitively *configured* [VERIFIED-LIVE]; the
   enforcement and provisioning posture determine how fragile a personal token is.
3. **Whether `elastic` permits machine/service GitHub accounts.** [UNVERIFIED]. This determines
   whether the leaver risk in §1.6 can be engineered away or only documented.
4. **The repository's default branch and directory layout.** `main` and a flat `advisories/` are
   assumptions. Both are confirmable in one request by anyone with access (§1.8 Step 2 returns
   `default_branch`; Step 3c lists the root tree) and both produce an indistinguishable 404 when
   wrong.
5. **The actual file count and file types in `advisories/`.** Determines whether the backfill is
   201 or 501 requests and whether a `file_pattern` filter is needed at all. Neither materially
   changes the conclusions above.
6. **Whether an organization-wide token audit or lifetime-policy change is scheduled at Elastic.**
   Either would silently break the integration. Worth asking, because the failure is a 404 and
   there is no alert for it.
7. **GHES applicability.** The GHES base URL form `http(s)://HOSTNAME/api/v3` is
   [VERIFIED-DOC], but fine-grained PAT availability, rate-limit configuration, and the exact
   permission model vary by GHES version. [UNVERIFIED] for any specific GHES release. The existing
   `github` package README states outright: *"This integration is not compatible with GitHub
   Enterprise server."* Making `api_url` configurable costs nothing and keeps the option open, but
   GHES support should not be claimed without testing.
