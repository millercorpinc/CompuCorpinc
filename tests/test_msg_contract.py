"""Validate that .MSG files in the inbox satisfy the inbox contract.

See docs/inbox-contract.md for the full specification.
"""

import re
from pathlib import Path

import pytest

INBOX = Path("work/C_WORK/MAIL/INBOX")

# YYYYMMDD_HHMMSS_<slug>__<ID>.MSG
FILENAME_RE = re.compile(r"^\d{8}_\d{6}_[a-z0-9-]+__[A-Za-z0-9_.:-]+\.MSG$")

REQUIRED_HEADERS = ["ID:", "FROM:", "TO:", "DATE:", "SUBJECT:"]

# DATE field must be YYYY-MM-DD HH:MM
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")


def _msg_files():
    if not INBOX.exists():
        return []
    return sorted(INBOX.glob("*.MSG"))


MSG_FILES = _msg_files()


@pytest.mark.parametrize("msg_path", MSG_FILES)
def test_filename_format(msg_path):
    assert FILENAME_RE.match(msg_path.name), (
        f"Filename does not match contract pattern: {msg_path.name}"
    )


@pytest.mark.parametrize("msg_path", MSG_FILES)
def test_required_headers(msg_path):
    text = msg_path.read_text(encoding="ascii", errors="replace")
    for header in REQUIRED_HEADERS:
        assert header in text, f"Missing header {header!r} in {msg_path.name}"


@pytest.mark.parametrize("msg_path", MSG_FILES)
def test_ends_with_end(msg_path):
    text = msg_path.read_text(encoding="ascii", errors="replace")
    assert "END:" in text, f"Missing END: sentinel in {msg_path.name}"


@pytest.mark.parametrize("msg_path", MSG_FILES)
def test_date_format(msg_path):
    text = msg_path.read_text(encoding="ascii", errors="replace")
    for line in text.splitlines():
        if line.startswith("DATE:"):
            date_val = line.split(":", 1)[1].strip()
            assert DATE_RE.match(date_val), (
                f"DATE field does not match YYYY-MM-DD HH:MM in "
                f"{msg_path.name}: {date_val!r}"
            )
            return
    pytest.fail(f"No DATE: line found in {msg_path.name}")
