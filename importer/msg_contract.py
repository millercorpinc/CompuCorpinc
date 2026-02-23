from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
from typing import Iterable

DATE_FMT = "%Y-%m-%d %H:%M"


@dataclass
class Message:
    message_id: str
    from_addr: str
    to_addr: str
    date: str
    subject: str
    body: str
    deliverables: list[str] | None = None
    definition_of_done: list[str] | None = None

    def validate(self) -> None:
        if not self.message_id.strip():
            raise ValueError("ID is required")
        if "@" not in self.from_addr:
            raise ValueError("FROM must be an email")
        if "@" not in self.to_addr:
            raise ValueError("TO must be an email")
        datetime.strptime(self.date, DATE_FMT)
        if not self.subject.strip():
            raise ValueError("SUBJECT is required")
        if not self.body.strip():
            raise ValueError("BODY is required")


def sanitize_slug(subject: str, max_len: int = 30) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", subject.lower()).strip("-")
    if not slug:
        slug = "no-subject"
    return slug[:max_len].rstrip("-")


def build_filename(dt: datetime, subject: str, message_id: str) -> str:
    return f"{dt.strftime('%Y%m%d_%H%M%S')}_{sanitize_slug(subject)}__{message_id}.MSG"


def format_msg(message: Message) -> str:
    message.validate()
    lines: list[str] = [
        f"ID: {message.message_id}",
        f"FROM: {message.from_addr}",
        f"TO: {message.to_addr}",
        f"DATE: {message.date}",
        f"SUBJECT: {message.subject}",
        "",
        "BODY:",
        message.body.rstrip(),
        "",
    ]
    if message.deliverables:
        lines.extend(["DELIVERABLES:", *[f"- {d}" for d in message.deliverables], ""])
    if message.definition_of_done:
        lines.extend(["DEFINITION_OF_DONE:", *[f"- {d}" for d in message.definition_of_done], ""])
    lines.append("END:")
    return "\n".join(lines) + "\n"


def parse_headers(raw: str) -> dict[str, str]:
    headers: dict[str, str] = {}
    body_seen = False
    for line in raw.splitlines():
        if not line.strip() and not body_seen:
            body_seen = True
            continue
        if body_seen:
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().upper()] = v.strip()
    return headers


def validate_msg_text(raw: str) -> None:
    required = ["ID:", "FROM:", "TO:", "DATE:", "SUBJECT:", "BODY:", "END:"]
    for token in required:
        if token not in raw:
            raise ValueError(f"missing required token {token}")
    h = parse_headers(raw)
    datetime.strptime(h.get("DATE", ""), DATE_FMT)


def read_processed_ids(inbox: Path, archive: Path, sent: Path) -> set[str]:
    ids: set[str] = set()
    for root in (inbox, archive, sent):
        if not root.exists():
            continue
        for path in root.glob("*.MSG"):
            text = path.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"^ID:\s*(.+)$", text, flags=re.MULTILINE)
            if m:
                ids.add(m.group(1).strip())
    return ids


def append_ledger(ledger_file: Path, filename: str, status: str) -> None:
    ledger_file.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.utcnow().strftime("%Y%m%d %H:%M")
    ledger_file.write_text(
        (ledger_file.read_text(encoding="utf-8") if ledger_file.exists() else "")
        + f"{now}  IMPORTED  {filename}  {status}\n",
        encoding="utf-8",
    )


def require_folders(paths: Iterable[Path]) -> None:
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)
