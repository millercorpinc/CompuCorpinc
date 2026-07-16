from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CODEX_BOOTSTRAP.md",
    "docs/START-HERE.md",
    "knowledge/MASTER-CONTEXT.md",
    "knowledge/DECISION-STATUS.md",
    "knowledge/OPEN-QUESTIONS.md",
    "docs/business/01-BUSINESS-DEFINITION.md",
    "docs/business/05-PARTNERSHIPS-AND-DISTRIBUTION.md",
    "docs/architecture/00-ARCHITECTURE-OVERVIEW.md",
    "docs/launch/00-LAUNCH-PROGRAM.md",
    "ops/launch-backlog.yaml",
]

INTENTIONAL_PLACEHOLDERS = {
    "[COMPANY_NAME]",
    "[SERVICE NAME]",
    "[PARTNER]",
    "[TITLE]",
}

def parse_skill_frontmatter(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{path.relative_to(ROOT)}: missing YAML frontmatter"]
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return [f"{path.relative_to(ROOT)}: malformed YAML frontmatter"]
    fm = match.group(1)
    for key in ("name:", "description:"):
        if key not in fm:
            errors.append(f"{path.relative_to(ROOT)}: missing {key[:-1]}")
    return errors

def markdown_links(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    links = []
    for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if target:
            links.append((label, target))
    return links

def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required file: {rel}")

    skill_files = sorted((ROOT / ".agents/skills").glob("*/SKILL.md"))
    if not skill_files:
        errors.append("No repository skills found")
    for path in skill_files:
        errors.extend(parse_skill_frontmatter(path))

    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".vendor"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"Empty Markdown file: {path.relative_to(ROOT)}")
        for label, target in markdown_links(path):
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                warnings.append(f"External relative path in {path.relative_to(ROOT)}: {target}")
                continue
            if not resolved.exists():
                errors.append(
                    f"Broken link in {path.relative_to(ROOT)}: {label} -> {target}"
                )

    # Flag common placeholders that are not part of templates or approved placeholders.
    placeholder_pattern = re.compile(r"\b(TODO|TBD|FIXME)\b")
    for path in ROOT.rglob("*.md"):
        if "templates" in path.parts or path.name == "ADR-0000-TEMPLATE.md":
            continue
        text = path.read_text(encoding="utf-8")
        for idx, line in enumerate(text.splitlines(), start=1):
            if placeholder_pattern.search(line):
                warnings.append(f"Placeholder in {path.relative_to(ROOT)}:{idx}: {line.strip()}")

    report = {
        "errors": errors,
        "warnings": warnings,
        "skill_count": len(skill_files),
        "markdown_count": len(list(ROOT.rglob("*.md"))),
    }
    (ROOT / "verification-report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

    print(json.dumps(report, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
