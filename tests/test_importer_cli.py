import json
from pathlib import Path

from importer.cli import pull_jsonl


def test_pull_jsonl(tmp_path: Path):
    src = tmp_path / "input.jsonl"
    src.write_text(
        json.dumps(
            {
                "message_id": "id-1",
                "from": "boss@company.com",
                "to": "ai@company.com",
                "date": "2026-02-22 09:14",
                "subject": "Task one",
                "body": "Do task one",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    work_root = tmp_path / "C_WORK"
    imported, skipped = pull_jsonl(src, work_root)
    assert imported == 1
    assert skipped == 0
    inbox_files = list((work_root / "MAIL" / "INBOX").glob("*.MSG"))
    assert len(inbox_files) == 1
