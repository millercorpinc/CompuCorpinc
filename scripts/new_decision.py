from pathlib import Path
import re
import sys
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "docs/decisions"
TEMPLATE = DECISIONS / "ADR-0000-TEMPLATE.md"

def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").upper()
    return value or "DECISION"

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python scripts/new_decision.py "Decision title"')
    title = " ".join(sys.argv[1:]).strip()
    numbers = []
    for path in DECISIONS.glob("ADR-*.md"):
        match = re.match(r"ADR-(\d{4})-", path.name)
        if match:
            numbers.append(int(match.group(1)))
    number = max(numbers, default=0) + 1
    filename = f"ADR-{number:04d}-{slugify(title)}.md"
    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("ADR-0000: Decision title", f"ADR-{number:04d}: {title}")
    text = text.replace("YYYY-MM-DD", date.today().isoformat(), 1)
    out = DECISIONS / filename
    out.write_text(text, encoding="utf-8")
    print(out.relative_to(ROOT))

if __name__ == "__main__":
    main()
