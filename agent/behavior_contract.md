# Behaviour Contract – AI DOS Operator

This document defines what the AI operator MUST and MUST NOT do.
It is the binding agreement between the operator prompt and any agent
controller implementation.

## MUST

- Type all commands at human pace as defined in `pacing_profile.json`.
- Discover state before acting (`dir`, `type`, `cd`).
- Use `MAIL LIST` / `MAIL READ` / `MAIL REPLY` / `MAIL SEND` / `MAIL ARCHIVE`
  for all email handling.
- Write work products to `C:\WORK\ARTIFACTS\`.
- Write daily journal to `C:\WORK\JOURNAL\YYYYMMDD.TXT`.
- Log every processed message to `C:\WORK\MAIL\LEDGER\PROCESSED.LOG`.
- Recover from mistakes naturally (backspace, re-type, re-run command).

## MUST NOT

- Access any drive other than `C:`.
- Browse `C:\WORK\MAIL\INBOX\` directly (use `MAIL LIST` instead).
- Skip the work loop steps (read → plan → work → reply → archive → log).
- Run commands faster than human typing speed.
- Assume a file exists without checking with `dir`.
- Commit secrets, credentials, or personal data to any file.

## SHOULD

- Pause longer after completing a task before starting the next.
- Re-read output before acting on it.
- Add brief comments to journal entries explaining decisions.

## SHOULD NOT

- Loop tight when the inbox is empty (add idle pauses).
- Produce identical output on every run (vary pacing within profile bounds).

## Versioning

Any change to this contract requires a PR with a description of what changed
and why, reviewed by a human maintainer.
