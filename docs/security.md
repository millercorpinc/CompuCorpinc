# Security and Compliance Baseline

## Threat model

- Inbox mail may contain sensitive business or personal data.
- Recordings may capture sensitive text on screen.
- Local model prompts/responses may include PII.

## Controls

1. Use local-only model runtime (Ollama bound to localhost).
2. Store mailbox credentials in environment variables, not repository files.
3. Restrict filesystem permissions on `work/C_WORK` to operator account only.
4. Enable log and recording retention purge via `scripts/retention_purge.sh`.
5. Keep `MAIL/LEDGER/PROCESSED.LOG` append-only.

## Secrets

- `GRAPH_TENANT_ID`
- `GRAPH_CLIENT_ID`
- `GRAPH_CLIENT_SECRET`
- `LOCAL_MODEL`
- `OLLAMA_URL`

## Retention policy (initial)

- `MAIL/ARCHIVE`: 30 days
- `MAIL/SENT`: 30 days
- `MAIL/FAILED`: 14 days
- recordings: 14 days (or shorter if policy requires)

## Incident response

1. Stop importer + controller services.
2. Snapshot `work/C_WORK/MAIL` and `ops/logs`.
3. Rotate secrets.
4. Review ledger and action logs for scope.
