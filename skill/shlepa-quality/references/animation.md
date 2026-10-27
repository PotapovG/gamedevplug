# Animation acceptance for ShlepaGame

## Failure to solve
The user observed captain's unnatural legs and distorted character arms in a real Core web v9.2 screenshot. Earlier ref2game joint-coordinate, cycle and critic tests had passed. Numeric continuity alone is thus insufficient.

## Required comparisons
Prepare synchronized A/B full-speed videos or equivalent frame sequences at **identical** native camera zoom, movement speed, hero and weapon, lighting, damage state and capture timing. If reference screenshot is supplied, preserve it as *baseline*, not as the acceptance benchmark. Compare to one authentic polished, similar-scale shipped 2D game example (respect copyright, link to source, do not embed unlicensed assets). Judge at player-visible size before magnification.

Test: idle 10 s, four and diagonal directional runs, 360-degree aiming at cardinal and diagonal targets, aim crossing vertical and horizontal, weapon recoil, attack impact, hit reaction, skin changes, and boss gait. Prefer 2 seconds before/after transition. Animated crops cannot replace full-stage viewing.

## Hard fail criteria (even if IK tests pass)
- Foot floats, digs or changes length, or switches grounded foot impossibly.
- Knee bending backward in a normal stride, stilt legs, feet divorced from torso weight or bizarre hip location.
- Arms detach, swing across face through bad layering, break at wrist or aim with a disconnected weapon.
- Hands shrink into pixel clusters, sleeves visibly slide, ugly joint caps, outline overlaps or holes.
- Puppet-like motion, extreme torsion not in the character's intended anatomy, ugly interpolation while crossing view direction.
- Sprite silhouette no longer resembles the character's approved original at normal play scale.

## Controlled alternatives
A: current WebGL2 cut-out IK rig; B: authored 4/8-direction pixel walk/run with only constrained procedural aiming arms; C optional: model/animate in Blender and render directional sprite sheets (3D→2D). The source of truth remains gameplay state. Disallow building a new renderer solely for this trial. Test one hero plus the captain (not the whole roster), and compare cost, asset volume, input responsiveness, visual quality and save independence.

## Generation prompt contract
Each generated part sheet should specify camera (top-down oblique 3/4), frame scale, limb root/hinge/end, straight neutral pose, distinct near/far overlap, boot sole and hand grip, alpha margins, protected silhouette, no pre-baked light/background, and exact runtime zoom. Approve a *neutral assembled pose* BEFORE splitting/generating many frames. If anatomy cannot meet constraints, reject and regenerate, not hack more invisible joint caps.

## Evidence labels
`AUTOMATED: PASS|FAIL|NOT_RUN`; `VISUAL: ACCEPT|REVISE|REJECT (critic name)`; `OWNER: ACCEPT|REJECT|PENDING`. These are separate, never combined into one 9/10 number.
