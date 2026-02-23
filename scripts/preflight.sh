#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="$ROOT/work/C_WORK"

required_dirs=(
  "$WORK/MAIL/INBOX" "$WORK/MAIL/OUTBOX" "$WORK/MAIL/SENT" "$WORK/MAIL/ARCHIVE"
  "$WORK/MAIL/FAILED" "$WORK/MAIL/LEDGER" "$WORK/JOURNAL" "$WORK/ARTIFACTS" "$WORK/NOTES"
)

for d in "${required_dirs[@]}"; do
  mkdir -p "$d"
  test -w "$d"
done

if command -v dosbox-x >/dev/null 2>&1; then
  echo "dosbox-x: OK"
else
  echo "dosbox-x: MISSING (install required)"
fi

if command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg: OK"
else
  echo "ffmpeg: MISSING (optional)"
fi

if command -v ollama >/dev/null 2>&1; then
  echo "ollama: OK"
else
  echo "ollama: MISSING (required for local AI controller)"
fi

echo "preflight complete"
