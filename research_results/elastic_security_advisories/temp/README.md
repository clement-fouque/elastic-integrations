# temp/ raw artifacts

Raw research artifacts retained for reproducibility.

Removed to avoid vendoring third-party source:

- `mito/` — a shallow clone of <https://github.com/elastic/mito>, the CEL evaluation library used by the Filebeat `cel` input. It was inspected to confirm which CEL extension functions exist (notably: mito provides HMAC but no RSA signing, so a CEL program cannot mint the RS256 JWT a GitHub App installation token requires). Re-obtain with `git clone https://github.com/elastic/mito`.
