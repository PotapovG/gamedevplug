#!/usr/bin/env python3
"""Descriptive boss-fight attack cadence from actual engine trace. Never a fun verdict."""
import argparse, collections, csv, json, pathlib, statistics

def analyze(p):
    with open(p,newline='',encoding='utf-8-sig') as f:
        reader=csv.DictReader(f)
        if not {'t','event','attack'}.issubset(reader.fieldnames or []):raise ValueError('Expected columns: t,event,attack')
        rows=[{'t':float(r['t']),'event':r['event'].strip().lower(),'attack':r['attack'].strip()} for r in reader]
    if not rows:raise ValueError('No data: cannot claim success')
    if any(r['t']<0 for r in rows):raise ValueError('Negative time')
    rows.sort(key=lambda r:r['t'])
    kinds=collections.Counter(r['attack'] for r in rows if r['event']=='tell' and r['attack'])
    pending={};times=[];last_end=None;gaps=[]
    for r in rows:
        if r['event']=='tell':pending[r['attack']]=r['t']
        if r['event']=='impact' and r['attack'] in pending:
            delta=r['t']-pending.pop(r['attack'])
            if delta>=0:times.append(delta)
        if r['event']=='tell' and last_end is not None and r['t']>=last_end:gaps.append(r['t']-last_end)
        if r['event'] in ('recover','attack_end'):last_end=r['t']
    duration=max(r['t'] for r in rows)-min(r['t'] for r in rows)
    warnings=[]
    if len(kinds)<3:warnings.append('Few distinct attacks observed; NOT proof of boring combat, investigate footage.')
    if gaps and max(gaps)>10:warnings.append('Gap >10s between attack recovery and next tell; inspect inactivity.')
    if times and statistics.median(times)>2:warnings.append('Median tell-to-impact >2s; investigate trivial dodging.')
    if not times:warnings.append('No paired tell→impact data; telegraph analysis unverified.')
    return {'source':str(p),'observed_seconds':round(duration,2), 'attack_counts':dict(kinds), 'distinct_attacks':len(kinds),
        'telegraph_pairs':len(times),'median_telegraph_s':round(statistics.median(times),3) if times else None,
        'max_recovery_to_next_tell_s':round(max(gaps),3) if gaps else None,
        'human_playtest':'NOT_VERIFIED', 'quality_verdict':'NOT_DETERMINED', 'warnings':warnings}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('events');p.add_argument('--out');a=p.parse_args()
    d=analyze(pathlib.Path(a.events));output=json.dumps(d,indent=2,ensure_ascii=False)+'\n'
    if a.out:pathlib.Path(a.out).write_text(output)
    print(output,end='')
