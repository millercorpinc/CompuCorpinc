from datetime import datetime

from importer.msg_contract import Message, build_filename, format_msg, sanitize_slug, validate_msg_text


def test_sanitize_slug():
    assert sanitize_slug("TASK: Inventory the WORK drive") == "task-inventory-the-work-drive"


def test_build_filename():
    dt = datetime(2026, 2, 22, 9, 14, 0)
    f = build_filename(dt, "TASK: Inventory the WORK drive", "2026-02-22-001")
    assert f.startswith("20260222_091400_task-inventory-the-work-drive__")


def test_render_and_validate():
    msg = Message(
        message_id="2026-02-22-001",
        from_addr="boss@company.com",
        to_addr="aiworker@company.com",
        date="2026-02-22 09:14",
        subject="TASK: Inventory the WORK drive",
        body="Please inventory C:\\WORK.",
    )
    raw = format_msg(msg)
    validate_msg_text(raw)
    assert "END:" in raw
