#!/usr/bin/env bash
set -euo pipefail

REF="${1:-main}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENDOR="$ROOT/.vendor/superpowers"
TARGET="$ROOT/.agents/skills"
MANIFEST="$TARGET/.superpowers-installed.txt"
VERSION="$TARGET/.superpowers-version"

command -v git >/dev/null 2>&1 || { echo "git is required"; exit 1; }

mkdir -p "$ROOT/.vendor" "$TARGET"

if [[ ! -d "$VENDOR/.git" ]]; then
  git clone https://github.com/obra/superpowers.git "$VENDOR"
else
  git -C "$VENDOR" fetch --all --tags --prune
fi

git -C "$VENDOR" checkout --force "$REF"
if [[ "$REF" == "main" ]]; then
  git -C "$VENDOR" pull --ff-only origin main
fi

# Remove only skill folders installed during the prior run.
if [[ -f "$MANIFEST" ]]; then
  while IFS= read -r skill; do
    [[ -z "$skill" ]] && continue
    [[ "$skill" == company-* ]] && continue
    rm -rf "$TARGET/$skill"
  done < "$MANIFEST"
fi

: > "$MANIFEST"

for dir in "$VENDOR"/skills/*; do
  [[ -d "$dir" ]] || continue
  skill="$(basename "$dir")"
  if [[ "$skill" == company-* ]]; then
    echo "Refusing upstream skill with reserved prefix: $skill"
    exit 1
  fi
  rm -rf "$TARGET/$skill"
  cp -R "$dir" "$TARGET/$skill"
  echo "$skill" >> "$MANIFEST"
done

git -C "$VENDOR" rev-parse HEAD > "$VERSION"
cp "$VENDOR/LICENSE" "$TARGET/SUPERPOWERS-LICENSE" 2>/dev/null || true

echo "Installed Superpowers skills at commit $(cat "$VERSION")"
echo "Open Codex from the repository root and run /skills."
