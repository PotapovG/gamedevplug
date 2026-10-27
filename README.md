# Shlepa Quality — Codex game-dev skill

A standalone Codex skill for animation QA, boss playtesting and blind A/B reviews in **ShlepaGame**.

This repository hosts a self-contained skill; it does **not** include, replace or modify `ref2game`.

## Install

```bash
git clone https://github.com/PotapovG/gamedevplug.git
cd gamedevplug
bash install.sh
```

Restart Codex and invoke `$shlepa-quality`. For QA, first work in a disposable branch or worktree, inspect the evidence, and do not merge or deploy without approval.

## Contents

- `skill/shlepa-quality/SKILL.md` — Codex entrypoint
- `skill/shlepa-quality/references/` — animation, boss design and QA policy
- `skill/shlepa-quality/scripts/` — session management, blind A/B, contact sheets and boss metrics
- `examples/` — event dataset
- `install.sh` — safe local install into `${CODEX_HOME:-~/.codex}/skills/`

This is a **quality harness**, not a replacement for human playtests or the game engine. See `NOTICE.md` for upstream inspirations and attribution.

MIT license. No production deployment or changes to ShlepaGame.
