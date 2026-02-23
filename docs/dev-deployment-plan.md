# Development and Deployment Plan

This document turns the existing DOS AI operator concept into an executable roadmap:
what to build, in what order, and what must be deployed to run reliably.

## 1) Current state summary

The repository already includes:

- A clear workstation architecture (`docs/architecture.md`).
- A file-backed inbox contract (`docs/inbox-contract.md`).
- Operational instructions (`docs/runbook.md`, `docs/troubleshooting.md`).
- A plan for Outlook import requirements (`docs/outlook-import-plan.md`).
- DOS-side mail tooling (`work/C_WORK/MAIL.BAT`) plus sample inbox data.

The largest remaining gaps are implementation and automation around:

1. Outlook importer implementation (currently design-only).
2. Agent controller implementation (currently external / out of repo).
3. Production deployment topology and observability.
4. Security + compliance controls around mailbox data and recordings.

## 2) Delivery goals

### Goal A — Repeatable local developer environment

Any engineer should be able to clone, launch DOSBox-X, ingest test mail, and validate
end-to-end flow in < 15 minutes.

### Goal B — Deterministic message processing pipeline

A message imported from Outlook should be traceable end-to-end:

`Outlook source -> INBOX .MSG -> AI processing -> OUTBOX/SENT + LEDGER`

### Goal C — Deployable operations profile

The system should run continuously on a designated host with:

- predictable startup/restart behavior,
- monitoring and alerting,
- backup and recovery procedures,
- documented incident response.

## 3) Workstreams and milestones

## Milestone 0: Baseline hardening (Week 1)

### Scope

- Validate all documented commands in `docs/runbook.md`.
- Ensure directories expected by DOS workflows exist by default.
- Add preflight checks script for host readiness.

### Deliverables

- `scripts/preflight.sh` (checks DOSBox-X path, writable `work/`, optional ffmpeg/OBS).
- Updated runbook section for "preflight and first boot".
- Smoke-test checklist markdown.

### Exit criteria

- Fresh machine can pass preflight and reach `MAIL LIST` without manual troubleshooting.

## Milestone 1: Outlook importer MVP (Weeks 1-2)

### Scope

Implement the external importer inside this repo (or a sibling service) using the contract in
`docs/outlook-import-plan.md`.

### Required features

- Source adapter (start with Graph API or `.pst` parser; pick one first).
- Deduplication by stable message ID.
- Filename sanitization according to contract.
- Body conversion to plain text.
- Error routing to `MAIL/FAILED`.
- Idempotent repeated runs.

### Deliverables

- `importer/` service with CLI:
  - `importer pull --since <timestamp>`
  - `importer backfill --folder Inbox --limit N`
- Unit tests for parsing, naming, and dedupe behavior.
- Integration test writing sample `.MSG` files to `work/C_WORK/MAIL/INBOX/`.

### Exit criteria

- Importer can ingest real mailbox data and produce contract-valid `.MSG` files.

## Milestone 2: Agent controller interface (Weeks 2-3)

### Scope

Define and implement the boundary between the external AI controller and this workstation.

### Required features

- Input contract for controller instructions / prompts.
- Event stream or logs for commands typed and outcomes.
- Safety policy for destructive DOS commands.
- Retry behavior for transient DOS failures.

### Deliverables

- `docs/controller-interface.md` contract.
- Reference adapter (CLI or local service) that drives DOSBox-X session.
- Replayable run logs stored under `work/C_WORK/NOTES/` or `ops/logs/`.

### Exit criteria

- A scripted scenario can run from message ingestion to drafted response autonomously.

## Milestone 3: Operations and deployment automation (Weeks 3-4)

### Scope

Package the host runtime as a managed service.

### Required features

- Service manager configuration (systemd on Linux / Task Scheduler on Windows).
- Centralized log capture and rotation.
- Heartbeat + stale inbox detection.
- Automated backup of `MAIL/`, `JOURNAL/`, `ARTIFACTS/`.

### Deliverables

- `deploy/systemd/` units and installation script (Linux-first).
- `ops/monitoring/` scripts:
  - inbox lag checker,
  - process health checker,
  - disk usage threshold alerts.
- Deployment runbook with rollback section.

### Exit criteria

- Host can reboot and return to healthy processing automatically.

## Milestone 4: Security/compliance and readiness (Week 5)

### Scope

Harden handling of potentially sensitive email content.

### Required features

- Secrets management for mailbox credentials.
- Data retention policy for inbox/outbox/logs/recordings.
- Access controls for `work/` and recordings directory.
- Redaction policy for exported artifacts and streams.

### Deliverables

- `docs/security.md` with threat model and controls.
- `.env.example` and secret-loading docs (no plaintext credentials in repo).
- Retention + purge script with dry-run mode.

### Exit criteria

- Security checklist signed off before production go-live.

## 4) Deployment architecture recommendation

Start with **single-host deployment** for speed, then evolve only if required.

## Phase 1: Single host (recommended initial)

Components on one machine:

- DOSBox-X workstation process
- Importer scheduled job
- Agent controller process
- Optional OBS/ffmpeg capture
- Local monitoring scripts + alert hooks

Pros: simple, low operational complexity.
Cons: single point of failure.

## Phase 2: Split ingestion and workstation

- Host A: importer + mailbox access + queue/fileshare output
- Host B: DOSBox-X + AI operator + recording

Pros: better isolation and security boundaries.
Cons: increased deployment complexity.

## 5) CI/CD plan

## CI checks (run on each PR)

- Markdown lint (`markdownlint`).
- Shell lint (`shellcheck`).
- Importer tests (once importer exists).
- Contract validation test: every `.MSG` fixture passes parser/validator.

## Release process

- Tag versions as `vYYYY.MM.DD`.
- Maintain `CHANGELOG.md` for operator-impacting changes.
- Keep rollback instructions per release.

## 6) Operational SLOs (initial)

- **Inbox freshness:** new message visible to DOS workflow within 60 seconds.
- **Processing success rate:** >= 99% over rolling 7 days.
- **Recovery time objective:** <= 30 minutes from host restart/failure.
- **Data durability:** daily backup with 7-day minimum retention.

## 7) Definition of production-ready

The project is ready for production when all are true:

1. Importer MVP is deployed and idempotent.
2. Agent controller interface is documented and tested.
3. Startup, monitoring, backup, and alerting are automated.
4. Security controls and retention policy are documented and active.
5. On-call runbook supports common incidents end-to-end.

## 8) Immediate next actions (this week)

1. Choose importer tech stack (Python recommended for mailbox + text tooling).
2. Create importer skeleton + `.MSG` validator based on `inbox-contract.md`.
3. Add host preflight script and wire it into runbook.
4. Add a minimal health-check script (`MAIL/INBOX` lag + process alive).
5. Schedule first end-to-end dry run with recorded evidence.
