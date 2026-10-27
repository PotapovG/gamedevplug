#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CODEX_HOME:-$HOME/.codex}/skills/shlepa-quality"
if [[ -e "$DEST" ]]; then
  echo "Already exists: $DEST" >&2
  echo "No overwrite. Back up / remove this exact skill yourself before reinstalling." >&2
  exit 2
fi
mkdir -p -- "$(dirname -- "$DEST")"
cp -R -- "$ROOT/skill/shlepa-quality" "$DEST"
python3 "$DEST/scripts/session.py" --help >/dev/null
python3 "$DEST/scripts/blind_ab.py" --help >/dev/null
python3 "$DEST/scripts/boss_metrics.py" --help >/dev/null
printf '\nInstalled shlepa-quality at %s\n' "$DEST"
echo 'Restart Codex or open a new session, then ask: Use $shlepa-quality to review the captain boss in read-only mode.'
echo 'No changes to ShlepaGame, Core or ref2game.'
