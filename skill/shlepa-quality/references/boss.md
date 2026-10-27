# Boss-fight acceptance: captain and pig

## Objective
Player must actively recognise and respond to distinct patterns while staying immersed. A 3–5 min target is optional pacing context, NOT a minimum artificial elapsed time.

## Gym harness
Use the REAL current game simulation and actual boss attacks/assets. Build or open an isolated gym on a development branch/temporary directory. Fast restart, seeded loadouts, one boss and fixed ground; selectable hero, curse level, items and upgrades; pause/save/resume; event export `t,event,attack` to CSV. Do not fake combat physics or deploy the gym in place of Core.

## Fail if
- Prolonged window of attacking a motionless target with no threat, choice or movement.
- Only two attack types repeat without interesting combinations/meaningful progression.
- Telegraph is so slow that reaction requires no commitment, or so short there is no fair counterplay.
- Defense has no visible physical/world cause; a second defense bar flickers blue/orange.
- Gameplay is instructed with text ("leave line", "break guard", numbered phases).
- Phase change is communicated primarily by UI rather than behaviour.
- Test passes solely on win rate, TTK, HP thresholds or one AI critic score.

## Scenario matrix
At minimum weak/typical/strong builds; 2+ heroes; curse 0 and 3 where appropriate; normal session plus one human-controlled run. Do not force equal wins or equal time across all builds. Include a failed human run, if natural, to study whether its cause can be understood.

## Human playtest card
- Did you ever feel safe just firing for 20+ seconds? When?
- Did you notice an attack pattern **from the boss's actions** rather than text?
- Were you required to change tactics? Which exact moment?
- Did you understand the source of any protection without a tooltip?
- Which mechanic was memorable? Which repeated until boring?
- Is the final minute more interesting than the first minute?

## Event log convention
CSV header: `t,event,attack`. Events `tell`, `impact`, `recover`, `attack_end` with t=game seconds; optional `damage_player`, `damage_boss`. Only events from the running combat count. `boss_metrics.py` outputs descriptive measurements and warnings; numerical evidence cannot decide fun. No claims from incomplete traces.
