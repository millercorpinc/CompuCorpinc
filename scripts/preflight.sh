#!/usr/bin/env bash
# Preflight checks – verify required tools and repo structure are in place.
# Run from the repository root:
#   bash scripts/preflight.sh

set -euo pipefail

PASS=0
FAIL=0

ok()   { echo "  OK  $1"; PASS=$((PASS + 1)); }
fail() { echo "FAIL  $1"; FAIL=$((FAIL + 1)); }

check_cmd() {
    if command -v "$1" >/dev/null 2>&1; then
        ok "$1 installed"
    else
        fail "$1 not found"
    fi
}

check_path() {
    if [ -e "$1" ]; then
        ok "$1"
    else
        fail "$1 missing"
    fi
}

echo "=== Preflight checks ==="
echo ""
echo "-- Tools --"
check_cmd dosbox-x
check_cmd ffmpeg
check_cmd shellcheck
check_cmd python3

echo ""
echo "-- Config --"
check_path ops/dosbox/dosbox-x.conf
check_path work/C_WORK/MAIL.BAT

echo ""
echo "-- Mail folders --"
check_path work/C_WORK/MAIL/INBOX
check_path work/C_WORK/MAIL/OUTBOX
check_path work/C_WORK/MAIL/SENT
check_path work/C_WORK/MAIL/ARCHIVE
check_path work/C_WORK/MAIL/FAILED
check_path work/C_WORK/MAIL/LEDGER

echo ""
echo "-- Work folders --"
check_path work/C_WORK/JOURNAL
check_path work/C_WORK/ARTIFACTS
check_path work/C_WORK/NOTES

echo ""
echo "Results: ${PASS} passed, ${FAIL} failed"
[ "$FAIL" -eq 0 ]
