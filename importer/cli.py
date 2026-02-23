from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

from importer.msg_contract import (
    DATE_FMT,
    Message,
    append_ledger,
    build_filename,
    format_msg,
    read_processed_ids,
    require_folders,
    validate_msg_text,
)


def stable_id(payload: dict) -> str:
    preferred = payload.get("message_id") or payload.get("id")
    if preferred:
        return str(preferred)
    blob = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


def pull_jsonl(source: Path, work_root: Path) -> tuple[int, int]:
    mail = work_root / "MAIL"
    inbox = mail / "INBOX"
    archive = mail / "ARCHIVE"
    sent = mail / "SENT"
    failed = mail / "FAILED"
    ledger = mail / "LEDGER" / "PROCESSED.LOG"
    require_folders([inbox, archive, sent, failed, ledger.parent])

    seen_ids = read_processed_ids(inbox, archive, sent)
    imported = 0
    skipped = 0

    for line in source.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        payload = json.loads(line)
        msg_id = stable_id(payload)
        if msg_id in seen_ids:
            skipped += 1
            continue
        try:
            dt = datetime.strptime(payload["date"], DATE_FMT)
            msg = Message(
                message_id=msg_id,
                from_addr=payload["from"],
                to_addr=payload["to"],
                date=payload["date"],
                subject=payload["subject"],
                body=payload["body"],
                deliverables=payload.get("deliverables"),
                definition_of_done=payload.get("definition_of_done"),
            )
            rendered = format_msg(msg)
            validate_msg_text(rendered)
            name = build_filename(dt, msg.subject, msg.message_id)
            (inbox / name).write_text(rendered, encoding="utf-8")
            append_ledger(ledger, name, "OK")
            seen_ids.add(msg_id)
            imported += 1
        except Exception as exc:
            failed_name = f"failed_{msg_id}.txt"
            (failed / failed_name).write_text(f"error: {exc}\npayload: {line}\n", encoding="utf-8")
            append_ledger(ledger, failed_name, f"FAILED:{exc}")
    return imported, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Outlook import MVP (JSONL source)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    pull = sub.add_parser("pull", help="Pull from JSONL export")
    pull.add_argument("--source", required=True, help="Path to JSONL messages")
    pull.add_argument("--work-root", default="work/C_WORK", help="Mounted WORK root")

    args = parser.parse_args()
    if args.cmd == "pull":
        imported, skipped = pull_jsonl(Path(args.source), Path(args.work_root))
        print(f"imported={imported} skipped={skipped}")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
