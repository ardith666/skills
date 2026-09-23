#!/bin/sh
# skills bootstrap — symlink semua skill dari repo ini ke ~/.agents/skills/
# Setiap skill punya SKILL.md di root folder-nya di repo ini.
set -e

SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${AGENT_SKILLS_DIR:-$HOME/.agents/skills}"

mkdir -p "$DEST"

for skill in diagram-design dev-methodology security-meth drawthings-adobestock mk-iticm obsidian-notes pptx-iticm uiux-methodology; do
  if [ ! -f "$SRC/$skill/SKILL.md" ]; then
    echo "skip $skill: SKILL.md tidak ada di $SRC/$skill/"
    continue
  fi
  if [ -L "$DEST/$skill" ]; then
    rm "$DEST/$skill"
  elif [ -e "$DEST/$skill" ]; then
    echo "skip $skill: $DEST/$skill bukan symlink (folder asli) — biarkan"
    continue
  fi
  ln -s "$SRC/$skill" "$DEST/$skill"
  echo "linked $skill -> $DEST/$skill"
done

echo "OK. Semua skill aktif."