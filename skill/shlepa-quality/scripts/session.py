#!/usr/bin/env python3
"""Create an isolated, auditable game-quality review. Python stdlib only."""
import argparse, json, os, pathlib, re, sys, time

KINDS = ('animation', 'boss', 'sprite-production')

def init(args):
    if not re.fullmatch(r'[a-z0-9][a-z0-9_.-]{0,70}', args.name):
        raise SystemExit('Invalid session name (lowercase letters, digits, ._- only).')
    base = pathlib.Path(args.out).expanduser().resolve()
    session = base / args.name
    if session.exists():
        raise SystemExit(f'Refusing overwrite of existing review: {session}')
    session.mkdir(parents=True)
    (session / 'before').mkdir()
    (session / 'after').mkdir()
    (session / 'evidence').mkdir()
    goal = {
        'animation':'Character anatomy looks convincing at actual gameplay scale.',
        'boss':'Boss fight creates meaningful decisions and readable threats, not a prolonged HP check.',
        'sprite-production':'Sprite production yields animation-ready silhouette and reproducible pivots.'
    }[args.kind]
    meta = {'name':args.name,'kind':args.kind,'source_sha':args.sha or 'UNVERIFIED',
            'goal':goal, 'created_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'auto_test':'NOT_RUN','critic':'PENDING','owner':'PENDING', 'scope':'no-main-no-core-no-release'}
    (session / 'session.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    criteria = {
        'animation': ['No broken or floating legs at native zoom','Hands and feet anatomically readable','No layer pops across 360 aim','Original silhouette survives every pose','Full-speed motion objectively better than baseline'],
        'boss': ['One health bar per boss','No mysterious guard or text advice','At least several distinct meaningful attack decisions','No long trivial downtime','Real human playtest finds fight engaging'],
        'sprite-production': ['Anchor character approved at actual gameplay scale','Hips/shoulders/pivots can be unambiguously identified','Animation remains sound in idle/run/attack','Reproducible generation prompt and source rights','Compared actual runtime rig variants before promotion']
    }[args.kind]
    rubric='# Frozen quality bar — '+args.name+'\n\nGoal: '+goal+'\n\n'
    rubric+='\n'.join('- [ ] '+x for x in criteria)+'\n\nAcceptance is FAIL if any visibly serious anatomy/gameplay defect remains. Do not lower these criteria after seeing output.\n'
    (session/'RUBRIC.md').write_text(rubric)
    (session/'VERDICT.md').write_text('''# Quality review\n\n## Baseline evidence\n\n- Source SHA:\n- Capture setup / camera / viewport:\n- Executed tests:\n\n## Improvements and regressions\n\n## Objective telemetry (not a fun score)\n\n## Independent visual/game critic\n\n- Critic identity:\n- Verdict: PENDING\n- Defects with frame/time evidence:\n\n## Owner real-play verdict\n\n- Owner: PENDING\n- What was fun / boring:\n\n## Decision\n\n- NOT APPROVED until user has seen the changed game.\n''')
    if args.kind=='boss':
        (session/'evidence'/'events-template.csv').write_text('t,event,attack\n')
    print(session)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='cmd', required=True)
    q=sub.add_parser('init')
    q.add_argument('--kind',choices=KINDS,required=True)
    q.add_argument('--name',required=True)
    q.add_argument('--sha',help='Actual baseline commit SHA')
    q.add_argument('--out',default='./quality-reviews')
    a=p.parse_args()
    if a.cmd=='init':init(a)
