# AGENTS.md

Operational guide for AI coding agents working in this fork of [elastic/integrations](https://github.com/elastic/integrations). This document is **fork-only** — it describes how to work locally in `clement-fouque/elastic-integrations`, not upstream contribution policy.

For human-oriented contribution guidance, see [CONTRIBUTING.md](CONTRIBUTING.md) and the [Integrations Developer Guide](https://www.elastic.co/guide/en/integrations-developer/current/index.html).

## Prerequisites

Before running any commands, verify:

- **Docker** (or Podman) is running.
- **`elastic-package`** is installed and available in `PATH`.

## Default scope

Work on **one integration package** at a time:

```bash
cd packages/<integration-name>
```

Or pass the package path from the repo root:

```bash
elastic-package -C packages/<integration-name> <command>
```

Repo-wide changes (`.github/`, `docs/`, `.agents/skills/`) are the exception — do not run package commands from the repo root unless scoped with `-C`.

## Package anatomy

Key paths inside `packages/<name>/`:

| Path | Purpose |
|------|---------|
| `manifest.yml` | Package metadata, version, conditions |
| `changelog.yml` | Release notes per version |
| `data_stream/<stream>/elasticsearch/ingest_pipeline/` | Ingest pipeline processors |
| `data_stream/<stream>/fields/` | Field definitions |
| `data_stream/<stream>/agent/stream/` | Agent input / stream templates |
| `data_stream/<stream>/_dev/test/pipeline/` | Pipeline test fixtures and expected JSON |
| `data_stream/<stream>/_dev/test/system/` | System test definitions |
| `data_stream/<stream>/_dev/deploy/` | Service definitions for system tests |
| `docs/README.md` | Rendered integration documentation |
| `_dev/build/docs/README.md` | Documentation source (edited before build) |

## Validate and build

Run from the package directory. Use the full explicit chain:

```bash
elastic-package format
elastic-package lint
elastic-package check
elastic-package build
```

Run this sequence before requesting a commit and after substantive changes.

## Stack and service lifecycle

Use the **minimal stack** required for the task. Never tear down running infrastructure without explicit user confirmation.

### Stack rules

1. **Check first** — run `elastic-package stack status` before starting or stopping the stack.
2. **Start only when needed** — see the test matrix below.
3. **Never run `elastic-package stack down` without asking the user** — even if tests fail or state looks stale.
4. **Reset only on request** — `stack down && stack up` is a deliberate reset, not a default step.

| Task | Stack command |
|------|---------------|
| `format`, `lint`, `check`, `build` | None |
| `test pipeline`, `test static` | `elastic-package stack up -d --services=elasticsearch` |
| `test system`, Fleet UI debugging | `elastic-package stack up -d` |

### Service rules

Packages with mock services (under `_dev/deploy/`) follow the same pattern:

1. **Check first** — run `elastic-package service status` (from the package directory).
2. **Start only for system tests** — `elastic-package service up` when `test system` or input/agent changes require it.
3. **Never run `elastic-package service down` without asking the user.**
4. Leave services running after successful tests unless the user asks to clean up.

## Test matrix

Run tests that match the change type. Do not run the full suite on every edit.

| You changed | Run |
|-------------|-----|
| Ingest pipeline, field mappings, parsing logic | `elastic-package test pipeline` |
| Pipeline test fixtures (updating expected output) | `elastic-package test pipeline --generate` (review diffs before keeping) |
| `manifest.yml`, Kibana dashboards, package assets | `elastic-package test asset` and `elastic-package test static` |
| Agent input config, CEL programs, stream templates | `elastic-package test system` (full stack + service if applicable) |
| Unsure or pre-commit | `format` → `lint` → `check` → `build`, plus `test pipeline` and `test static` at minimum |

### Test commands reference

```bash
elastic-package test pipeline
elastic-package test static
elastic-package test asset
elastic-package test system
```

## Skills

Read the relevant skill before making non-trivial changes. Repo skills live in [`.agents/skills/`](.agents/skills/); install them with:

```bash
npx skills@latest add https://github.com/elastic/integrations/tree/main/.agents/skills
```

Personal Cursor skills (available in this environment) complement the repo skills:

| Task | Skill |
|------|-------|
| `elastic-package` commands, stack, services | `elastic-package-cli` |
| Ingest pipeline processors and parsing | `ingest-pipelines` |
| ECS field mapping decisions | `ecs-field-mappings` |
| Pipeline and system test setup | `integration-testing` |
| Creating or reviewing integrations | `create-integration`, `maintain-integration`, `review-integration` |
| Package spec and manifest structure | `package-spec` |
| CEL input programs | `cel-programs` |
| Anonymizing real log samples for fixtures | `anonymize-logs` |
| Docs linting with vale | `validate-integration-docs` (repo) |
| Migrating to required input dependencies | `migrate-required-input-dependency` (repo) |

## Git rules

**Default: explore and edit locally only.**

- Do **not** commit, push, or open pull requests unless the user explicitly asks.
- Do **not** bump `manifest.yml` version or edit `changelog.yml` during iteration.

### When the user asks to commit

1. Run the full validate chain (`format` → `lint` → `check` → `build`).
2. Run the test matrix entries relevant to the changes.
3. Add a `changelog.yml` entry following the existing format in the package.
4. Bump `version` in `manifest.yml`.
5. Update `docs/README.md`, sample events, and field definitions if fields or behavior changed.
6. Commit and push to **`origin` only** — the user handles upstream PRs to `elastic/integrations` separately.

## Test data

- Prefer **synthetic** or already-anonymized fixtures in `_dev/test/`.
- When adapting real log samples, **anonymize PII and secrets** before they land in test files. Use the `anonymize-logs` skill.
- The user reviews all changes before any commit.

## Troubleshooting

| Symptom | Action |
|---------|--------|
| `lint` fails on formatting | Run `elastic-package format`, then `lint` again |
| `check` fails after a clean `lint` | Read the specific error — often a missing field definition or invalid manifest reference |
| Pipeline test mismatch | Run `elastic-package test pipeline --generate`, review the diff, keep only intentional changes |
| System test cannot reach service | Check `elastic-package service status`; start with `service up` if not running |
| Stack version mismatch | Check `conditions.kibana.version` in `manifest.yml`; align with `elastic-package stack up --version` if needed |
| Stale stack state | **Ask the user** before running `stack down` |

## References

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [Integrations Developer Guide](https://www.elastic.co/guide/en/integrations-developer/current/index.html)
- [Package specification](https://github.com/elastic/package-spec)
- [elastic-package repository](https://github.com/elastic/elastic-package)
- [Repo agent skills](.agents/skills/README.md)
