# Agent Instructions (MUST FOLLOW)

## Goal

Create and maintain a DOSBox-X workstation mounted to `work/C_WORK`, with a
file-backed `MAIL` inbox and realism operator docs, so that an AI can operate
it like a human office worker.

## Non-negotiables

- Keep `/ops`, `/docs`, `/agent`, `/work` structure stable.
- All scripts must be idempotent.
- Every change must update the runbook (`docs/runbook.md`) if it affects
  setup or run steps.
- Prefer small PRs: one topic per PR.
- Shell scripts must pass ShellCheck before merge.
- Markdown must pass markdownlint before merge.

## Definition of Done (v1)

- Launch DOSBox-X with `ops/dosbox/dosbox-x.conf`; it mounts `C:\WORK`.
- Typing `MAIL LIST` shows inbox files from `C:\WORK\MAIL\INBOX`.
- `MAIL READ`, `MAIL REPLY`, and `MAIL ARCHIVE` work end-to-end.
- OBS notes and ffmpeg script exist and are runnable.
- Docs cover inbox schema and operator realism rules.

## Folder contract

| Host path                  | DOS path           | Purpose                       |
| -------------------------- | ------------------ | ----------------------------- |
| `work/C_WORK/`             | `C:\WORK\`         | Workstation root              |
| `work/C_WORK/MAIL/INBOX/`  | `C:\WORK\MAIL\INBOX\`  | Incoming mail (.MSG files) |
| `work/C_WORK/MAIL/OUTBOX/` | `C:\WORK\MAIL\OUTBOX\` | AI-drafted replies         |
| `work/C_WORK/MAIL/SENT/`   | `C:\WORK\MAIL\SENT\`   | Sent mail archive          |
| `work/C_WORK/MAIL/ARCHIVE/`| `C:\WORK\MAIL\ARCHIVE\`| Processed inbox archive    |
| `work/C_WORK/JOURNAL/`     | `C:\WORK\JOURNAL\`     | AI daily journals          |
| `work/C_WORK/ARTIFACTS/`   | `C:\WORK\ARTIFACTS\`   | Work products              |
| `work/C_WORK/NOTES/`       | `C:\WORK\NOTES\`       | Scratch notes              |

## Coding style

- Bash: POSIX-ish, `set -euo pipefail`, ShellCheck-clean.
- DOS batch: `@echo off` at top, labels for each sub-command.
- Markdown: ATX headings, fenced code blocks with language hints.
- JSON: 2-space indent, no trailing commas.

## Issue labels

- `bug` – something broken
- `enhancement` – new feature
- `docs` – documentation only
- `ci` – workflow changes
