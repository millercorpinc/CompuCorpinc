#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INBOX="$ROOT/work/C_WORK/MAIL/INBOX"
LEDGER="$ROOT/work/C_WORK/MAIL/LEDGER/PROCESSED.LOG"
MAX_AGE_MIN="${MAX_INBOX_AGE_MIN:-60}"

if [ ! -d "$INBOX" ]; then
  echo "CRIT: inbox missing"
  exit 2
fi

latest_file="$(find "$INBOX" -maxdepth 1 -name '*.MSG' -type f -printf '%T@ %f\n' 2>/dev/null | sort -nr | head -n1 | awk '{print $2}')"
if [ -n "$latest_file" ]; then
  latest_epoch="$(stat -c %Y "$INBOX/$latest_file")"
  now_epoch="$(date +%s)"
  age_min=$(( (now_epoch - latest_epoch) / 60 ))
  if [ "$age_min" -gt "$MAX_AGE_MIN" ]; then
    echo "WARN: latest inbox message age ${age_min}m exceeds ${MAX_AGE_MIN}m"
  else
    echo "OK: inbox freshness ${age_min}m"
  fi
else
  echo "WARN: no inbox messages"
fi

if [ -f "$LEDGER" ]; then
  echo "OK: ledger present"
else
  echo "WARN: ledger missing"
fi
