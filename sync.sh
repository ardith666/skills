#!/bin/sh
# Sync mirror diagram-design dari upstream, lalu refresh snapshot di repo skills.
set -e

MIRROR_DIR="${MIRROR_DIR:-$HOME/code/diagram-design-mirror}"

echo "== 1/2 sync mirror diagram-design dari upstream =="
if [ -d "$MIRROR_DIR/.git" ]; then
  cd "$MIRROR_DIR"
  git fetch upstream 2>/dev/null || git remote add upstream https://github.com/cathrynlavery/diagram-design.git && git fetch upstream
  git push origin --mirror
else
  echo "MIRROR_DIR=$MIRROR_DIR tidak ada. Skip mirror sync. Clone dulu:"
  echo "  git clone --bare https://github.com/cathrynlavery/diagram-design.git $MIRROR_DIR"
  echo "  cd $MIRROR_DIR && git remote add upstream https://github.com/cathrynlavery/diagram-design.git"
  echo "  git push --mirror https://github.com/ardith666/diagram-design.git"
fi

echo "== 2/2 refresh snapshot diagram-design di repo skills =="
cd "$(dirname "$0")"
rsync -a --delete --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' --exclude '.env' \
  "$MIRROR_DIR" ./diagram-design/ 2>/dev/null || echo "SKIP: mirror belum ada — clone manual dari ardith666/diagram-design"
git add -A
git -c commit.gpgsign=false commit -m "sync diagram-design snapshot $(date +%Y-%m-%d)" 2>/dev/null || echo "tidak ada perubahan"
git push

echo "OK. Update mesin lain: cd skills && git pull && ./setup.sh"