"""Tests for scripts/import_msg.py"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

IMPORTER = Path("scripts/import_msg.py")
FILENAME_RE = re.compile(r"^\d{8}_\d{6}_[a-z0-9-]+__[A-Za-z0-9_.:-]+\.MSG$")


def _run(tmp_inbox: Path, extra: list | None = None) -> subprocess.CompletedProcess:
    cmd = [
        sys.executable,
        str(IMPORTER),
        "--from", "boss@company.com",
        "--to", "worker@company.com",
        "--subject", "Test subject",
        "--body", "Hello body.",
        "--inbox", str(tmp_inbox),
    ]
    if extra:
        cmd.extend(extra)
    return subprocess.run(cmd, capture_output=True, text=True)


def test_creates_msg_file(tmp_path):
    result = _run(tmp_path)
    assert result.returncode == 0
    assert len(list(tmp_path.glob("*.MSG"))) == 1


def test_filename_format(tmp_path):
    _run(tmp_path)
    files = list(tmp_path.glob("*.MSG"))
    assert FILENAME_RE.match(files[0].name), f"Bad filename: {files[0].name}"


def test_required_headers_present(tmp_path):
    _run(tmp_path)
    content = list(tmp_path.glob("*.MSG"))[0].read_text()
    for header in ["ID:", "FROM:", "TO:", "DATE:", "SUBJECT:", "BODY:", "END:"]:
        assert header in content, f"Missing header: {header}"


def test_body_content(tmp_path):
    _run(tmp_path)
    content = list(tmp_path.glob("*.MSG"))[0].read_text()
    assert "Hello body." in content


def test_deduplication_by_id(tmp_path):
    _run(tmp_path, ["--id", "dedup-test-001"])
    _run(tmp_path, ["--id", "dedup-test-001"])
    files = list(tmp_path.glob("*.MSG"))
    assert len(files) == 1, "Deduplication failed: duplicate file was created"


def test_custom_id_in_filename(tmp_path):
    _run(tmp_path, ["--id", "my-custom-id"])
    files = list(tmp_path.glob("*.MSG"))
    assert "my-custom-id" in files[0].name


def test_custom_id_in_content(tmp_path):
    _run(tmp_path, ["--id", "explicit-id-xyz"])
    content = list(tmp_path.glob("*.MSG"))[0].read_text()
    assert "ID: explicit-id-xyz" in content


def test_creates_inbox_dir_if_missing(tmp_path):
    inbox = tmp_path / "nested" / "INBOX"
    result = _run(inbox)
    assert result.returncode == 0
    assert inbox.exists()


def test_output_message_on_success(tmp_path):
    result = _run(tmp_path)
    assert result.stdout.startswith("OK:")


def test_skip_message_on_duplicate(tmp_path):
    _run(tmp_path, ["--id", "dup-id"])
    result = _run(tmp_path, ["--id", "dup-id"])
    assert "SKIP:" in result.stdout
