---
name: shlepa-quality
description: Independent game-quality skill for ShlepaGame. Use for boss-fight feel, combat gyms, animation/rig diagnostics, blind A/B comparisons, sprite production gates and practical playtest evidence. Complements ref2game but NEVER installs, changes or imports it. Does not replace the game's Codex Goal.
---

# Shlepa Quality — an independent Codex quality studio

This is a **separate skill**, not a game engine. Preserve the existing game, ref2game, WebGL2 rendering, repositories and release processes. It helps catch failures that geometry tests or victory rates miss: ugly body poses, unfun bosses, unreadable animation, exposed spoilers. The owner is the final judge of taste.

## Hard rules

1. **The skill itself must not autonomously alter `main`, Core, prod, secrets, saves, Codex Goal or the ref2game installation.** Work on an isolated worktree/branch for experimental QA and animation alternatives. Read-only inspection and local capture are fine. Its QA verdict is advisory; a parent *existing* continuous Goal may perform its own authorized routine source merge after real checks, while production/public release remains permission-gated. Never create a competing Goal.
2. **Visual correctness is not a joint-coordinate pass.** If knees are technically continuous but look broken at actual game zoom, the animation FAILS. A reviewer score is evidence, not approval.
3. **Fun is not TTK.** Winning 18/20 automated runs, a 3–5 minute boss TTK or a high critic score cannot establish enjoyment. Track empty downtime, pattern diversity, meaningful decisions, threat and human feedback. A long, boring fight FAILS.
4. **No text RPG.** Do not replace readable combat with HUD tutorials revealing boss attacks, phase numbers or player instructions. Express attacks and guard origins diegetically via pose, action, sounds and effects. Narrative dialogue remains narrative.
5. **One boss health bar only.** If defense exists it must have an in-world source; never disguise additional hit points, invulnerability or hard DPS caps as depth.
6. **Cost-aware and release-cadence aware.** One targeted critic per review round, maximum 3 rounds by default, no recursive agents. When the project activates its 2026-10-27 policy, preserve working vX.1...vX.9 and the next v(X+1).0 real private playable build; never accidentally trigger an old .5 build. Do not start an additional Goal or a nightly loop automatically. Read ShlepaGame's current AGENTS.md and CONTINUOUS_GOAL.md instead of treating this skill as an alternate Goal coordinator.
7. **No forced technology choice.** Compare (A) current cut-out rig, (B) hybrid authored gait + procedural weapon aim, optionally (C) pre-rendered 3D→2D frames. Keep actual sprite style, design and combat control identical. Change an engine only after evidence.
8. **Honest gates.** Distinguish automated PASS, reviewer opinion and human owner approval. A missing video or real player test is **UNVERIFIED**, never PASS.

## Work modes

- **`animation`**: Start an isolated visual review. Use real hero/boss screenshots at identical camera, scale and timing; capture idle, stride, cardinal and diagonal aim, hands/weapons, transitions, damage pose. Load `references/animation.md`. Run blind A/B on pre-rendered captures with `scripts/blind_ab.py`. Include a native-resolution contact sheet plus video (video can be referenced but tool does not generate one).
- **`boss`**: Build a *playable, minimal* battle gym using the **actual game simulation** and its rules, not a separate approximate combat engine. Isolate scene/player/boss into a harness; make loadout, curse and speed tunable. Do not alter the production campaign for a test harness. Load `references/boss.md`. Capture attack event logs and use `scripts/boss_metrics.py` for indicators; humans decide if the fight is fun.
- **`sprite-production`**: Analyse source assets, view angles, roots, pivots and silhouette at play size. Evaluate whether current sliced parts can ever animate cleanly. Propose new generation prompts and 2–3 controlled prototypes (cut-out vs hybrid). Load `references/animation.md`. Do not overwrite original art or regenerate the entire roster on speculation.
- **`blind-review`**: Produce randomized A/B files, collect a reviewer verdict, cryptographically lock it before revealing labels. `scripts/blind_ab.py` enforces verdict immutability after lock. The reviewer should not see `private/`.
- **`read-only-audit`**: Diagnose and report only. Do not prepare mutating tools.

## Minimal workflow

1. Ground the *current SHA* and exact player-visible symptom; read the relevant issue/task ID and existing test results. Avoid reading unrelated repo history.
2. Choose one mode. Generate a review folder **outside the game**:
   `python3 <skill>/scripts/session.py init --kind animation --name hero-rig-v9 --out /tmp/shlepa-quality/reviews`
   or `--kind boss --name captain-v9`.
3. Before edits, save baseline captures and a rubric with explicit fail criteria; never move the bar after viewing output. Use actual runtime screenshots and input traces.
4. Make a minimal prototype on a separate branch only when authorized. Maintain baseline source and save compatibility.
5. Get measurable checks + full-speed gameplay captures + one independent critique. For major player-facing changes, request **human playtest** instead of letting the agent mark quality as accepted.
6. Record exact test commands, assets and code SHAs. If incomplete, leave `HUMAN: PENDING`. Stop after three rounds unless the owner asks to continue.

## Scripts

- `session.py`: creates a self-contained review session and frozen acceptance rubric with examples.
- `blind_ab.py`: `prepare` → `lock` → `reveal` for genuinely blind A/B.
- `boss_metrics.py`: analyse actual boss event CSV (attack diversity, telegraph delay and inactivity indicators).
- `contact_sheet.py`: image collage at the same zoom (Pillow optional), preserving source files.

Run `python3 <skill>/scripts/<script>.py --help`. Python 3.9+; standard library for all except Pillow-based contact sheets. Installation requires no engine dependency.

## Important scope notes

This skill is authored specifically for ShlepaGame, inspired by (not copying) `studioigor/game-exp-skills`, `studioigor/studioigor-skill`, and `studioigor/gamestudio`. Their originals are not bundled. The optional external Codex `gauntlet-loop` skill can be installed separately if the owner wants its full long-run machinery, but is not required by this skill. **ref2game is not included, not installed, not changed.**

Do not introduce a replacement producer/coordinator or new mandatory ceremonies. Integration is opt-in per named task. Follow existing project `AGENTS.md` unless its rules would cause a known visual/UI regression; surface those conflicts to the owner, do not silently overrule them.
