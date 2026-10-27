# Lean workflow (adapted principles)

Use the existing ShlepaGame PR/test/release process. Keep this work bounded:
- One highest-impact player-visible flaw at a time.
- One critic per round, rotating visual/motion/game-feel lenses; max 3 rounds.
- Risk-weighted tests: saves/timers/physics need regression tests; colors and labels need a focused browser screenshot, not an architecture committee.
- Track `source SHA`, before/after capture, executed commands, risks and an explicit owner verdict.
- Stop measuring if no player-visible delta is expected; measure the actual improvement rather than tokens used to measure tokens.
- A senior toolchain cannot substitute for an aesthetically convincing screenshot. If the player sees broken knees, visual acceptance is FAIL.
- Never merge, deploy or start a new long-running Goal on a review-only request.
