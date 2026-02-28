#!/usr/bin/env python3
"""inject-msg: create a .MSG file in the file-backed inbox.

Usage:
  python scripts/import_msg.py \\
    --from boss@company.com \\
    --to aiworker@company.com \\
    --subject "TASK: Do something" \\
    --body "Please do something." \\
    [--id custom-id] \\
    [--inbox work/C_WORK/MAIL/INBOX]

The script is idempotent: running it twice with the same --id (or the same
derived hash) will not create a duplicate file.
"""

import argparse
import hashlib
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def slugify(text: str, max_len: int = 30) -> str:
    """Convert text to a lowercase, hyphen-separated slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


def derive_id(from_addr: str, subject: str, date_str: str) -> str:
    """Return a short deterministic ID derived from the key headers."""
    raw = f"{from_addr}|{subject}|{date_str}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def build_filename(date_utc: datetime, slug: str, msg_id: str) -> str:
    """Return: YYYYMMDD_HHMMSS_<slug>__<id>.MSG"""
    ts = date_utc.strftime("%Y%m%d_%H%M%S")
    return f"{ts}_{slug}__{msg_id}.MSG"


def build_content(
    msg_id: str,
    from_addr: str,
    to_addr: str,
    date_utc: datetime,
    subject: str,
    body: str,
) -> str:
    """Return the full .MSG file content per the inbox contract."""
    date_str = date_utc.strftime("%Y-%m-%d %H:%M")
    lines = [
        f"ID: {msg_id}",
        f"FROM: {from_addr}",
        f"TO: {to_addr}",
        f"DATE: {date_str}",
        f"SUBJECT: {subject}",
        "",
        "BODY:",
        body.strip(),
        "",
        "END:",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------


def inject(args: argparse.Namespace) -> int:
    inbox = Path(args.inbox)
    inbox.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d %H:%M")
    slug = slugify(args.subject)
    msg_id = args.id or derive_id(args.from_addr, args.subject, date_str)

    filename = build_filename(now, slug, msg_id)

    # Deduplication: skip if any existing file contains this ID
    for existing in inbox.glob("*.MSG"):
        text = existing.read_text(encoding="ascii", errors="replace")
        if f"ID: {msg_id}" in text:
            print(f"SKIP: ID {msg_id!r} already exists ({existing.name}).")
            return 0

    dest = inbox / filename
    content = build_content(
        msg_id, args.from_addr, args.to_addr, now, args.subject, args.body
    )
    dest.write_text(content, encoding="ascii", errors="replace")
    print(f"OK: {filename}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inject a .MSG file into the file-backed inbox.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--from", dest="from_addr", required=True, metavar="ADDRESS",
        help="Sender email address",
    )
    parser.add_argument(
        "--to", dest="to_addr", required=True, metavar="ADDRESS",
        help="Recipient email address",
    )
    parser.add_argument("--subject", required=True, help="Subject line")
    parser.add_argument("--body", required=True, help="Message body text")
    parser.add_argument(
        "--id", default=None, metavar="ID",
        help="Override message ID (default: SHA-256 hash of key headers)",
    )
    parser.add_argument(
        "--inbox",
        default="work/C_WORK/MAIL/INBOX",
        metavar="DIR",
        help="Path to inbox directory (default: work/C_WORK/MAIL/INBOX)",
    )
    return inject(parser.parse_args())


if __name__ == "__main__":
    sys.exit(main())
