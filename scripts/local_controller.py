#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "C_WORK"
INBOX = WORK / "MAIL" / "INBOX"
LOG = ROOT / "ops" / "logs" / "controller-actions.log"
PROMPT_FILE = ROOT / "agent" / "operator_prompt.txt"
MODEL = os.getenv("LOCAL_MODEL", "llama3.1:8b-instruct-q4_K_M")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")


def latest_message() -> Path | None:
    files = sorted(INBOX.glob("*.MSG"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def ask_model(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2, "num_predict": 512},
    }
    req = Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urlopen(req, timeout=120) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body.get("response", "")


def is_blocked(text: str) -> bool:
    banned = ["FORMAT", "DELTREE", "FDISK", "SYS C:"]
    u = text.upper()
    return any(b in u for b in banned)


def main() -> int:
    msg = latest_message()
    if not msg:
        print("no inbox messages")
        return 0

    operator_prompt = PROMPT_FILE.read_text(encoding="utf-8", errors="replace")
    mail = msg.read_text(encoding="utf-8", errors="replace")
    prompt = (
        f"{operator_prompt}\n\n"
        "Generate a safe DOS task plan with numbered steps and commands only under C:\\WORK.\n\n"
        f"MESSAGE:\n{mail}\n"
    )

    plan = ask_model(prompt)
    verdict = "BLOCKED" if is_blocked(plan) else "OK"

    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"=== {msg.name} [{verdict}] ===\n{plan}\n\n")

    print(verdict)
    return 2 if verdict == "BLOCKED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
