#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGETS=(
  "$ROOT/work/C_WORK/MAIL/ARCHIVE"
  "$ROOT/work/C_WORK/MAIL/SENT"
  "$ROOT/work/C_WORK/MAIL/FAILED"
)
RETENTION_DAYS="${RETENTION_DAYS:-30}"
DRY_RUN="${DRY_RUN:-1}"

for t in "${TARGETS[@]}"; do
  [ -d "$t" ] || continue
  if [ "$DRY_RUN" = "1" ]; then
    find "$t" -type f -mtime "+$RETENTION_DAYS" -print
  else
    find "$t" -type f -mtime "+$RETENTION_DAYS" -delete
  fi
done
