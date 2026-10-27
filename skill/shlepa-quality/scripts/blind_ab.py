#!/usr/bin/env python3
"""Prepare reproducible randomized blind A/B, lock verdict BEFORE reveal."""
import argparse, hashlib, json, os, pathlib, random, shutil, sys

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def prep(a):
    srcs=[pathlib.Path(a.a).resolve(),pathlib.Path(a.b).resolve()]
    if not all(p.is_file() for p in srcs):raise SystemExit('Both source files must exist.')
    d=pathlib.Path(a.out).resolve()
    if d.exists():raise SystemExit('Session exists: no overwrite.')
    (d/'public').mkdir(parents=True)
    (d/'private').mkdir()
    order=list(range(2));random.SystemRandom().shuffle(order)
    for label,k in zip('AB',order):shutil.copy2(srcs[k],d/'public'/f'{label}{srcs[k].suffix.lower()}')
    secret={'A':str(srcs[order[0]]),'B':str(srcs[order[1]]),'source_sha256':{str(x):sha(x) for x in srcs}}
    key=d/'private'/'key.json';key.write_text(json.dumps(secret,indent=2)+'\n');os.chmod(key,0o600)
    (d/'public'/'verdict.md').write_text('''# Blind A/B verdict\n\nReviewer (not builder):\nCriterion and baseline: \nNative resolution / camera: \nA score / observed defects: \nB score / observed defects: \nWinner and why: \n\nWrite a clear verdict before the builder runs `lock`.\n''')
    print('Public review folder:',d/'public');print('Keep private/ hidden from reviewer. Run lock THEN reveal.')

def lock(a):
    d=pathlib.Path(a.dir).resolve();verdict=d/'public'/'verdict.md';lockfile=d/'private'/'locked.json'
    if not (d/'private'/'key.json').is_file() or not verdict.is_file():raise SystemExit('Not a valid review.')
    if lockfile.exists():raise SystemExit('Verdict already locked.')
    data=verdict.read_text()
    required=['Reviewer (not builder):','Criterion and baseline:',
              'Native resolution / camera:','A score / observed defects:',
              'B score / observed defects:','Winner and why:']
    lines=data.splitlines()
    for field in required:
        matches=[line for line in lines if line.startswith(field)]
        if len(matches)!=1 or not matches[0][len(field):].strip():
            raise SystemExit(f'Unfilled or duplicate verdict field: {field}')
    payload={'verdict_sha256':sha(verdict),'verdict_bytes':verdict.stat().st_size}
    lockfile.write_text(json.dumps(payload,indent=2)+'\n');os.chmod(lockfile,0o600)
    print('Locked verdict SHA256:',payload['verdict_sha256'])

def reveal(a):
    d=pathlib.Path(a.dir).resolve();lockfile=d/'private'/'locked.json'
    if not lockfile.is_file():raise SystemExit('Verdict must be locked first.')
    lockdata=json.loads(lockfile.read_text());v=d/'public'/'verdict.md'
    if sha(v)!=lockdata['verdict_sha256']:
        raise SystemExit('Verdict changed since lock: AB REVEAL REFUSED.')
    keys=json.loads((d/'private'/'key.json').read_text());print('VERDICT (locked):',v)
    for label in 'AB':print(label,'=',keys[label])

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='action',required=True)
    s=sub.add_parser('prepare');s.add_argument('--a',required=True);s.add_argument('--b',required=True);s.add_argument('--out',required=True)
    for act in ('lock','reveal'):
        s=sub.add_parser(act);s.add_argument('--dir',required=True)
    args=p.parse_args();{'prepare':prep,'lock':lock,'reveal':reveal}[args.action](args)
