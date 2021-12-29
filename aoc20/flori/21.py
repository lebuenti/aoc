#!/usr/bin/env python3

from collections import defaultdict, Counter

with open('21.in', 'r') as f:
	ll = f.read().splitlines()

Cs = defaultdict(Counter)
ALLERGS = set()
INGRS = set()
COMPLETE = []

for l in ll:
  sp = l[:-1].split(' (contains')
  ingrs = [w.strip() for w in sp[0].split(' ')]
  allergs = [w.strip() for w in sp[1].split(', ')]
  ALLERGS |= set(allergs)
  INGRS |= set(ingrs)
  for ingr in ingrs:
    Cs[ingr] += Counter(allergs)
  COMPLETE.append((ingrs, allergs))

MX = {}
for a in ALLERGS:
  mx,sub = -1, set()
  for k in Cs:
    if Cs[k][a] > mx:
      mx = Cs[k][a]
      sub = {k}
    elif Cs[k][a] == mx:
      sub.add(k)
  MX[a] = sub

assert len(MX) == len(ALLERGS)

mxes = set([x for k in MX.values() for x in k])
GOOD = {ing for ing in INGRS if ing not in mxes}
print(len([i for i,_ in COMPLETE for ing in i if ing in GOOD]))

dones = set()
while len(dones) == len(MX):
  single = None
  for k in MX:
    cand = next(iter(MX[k]))
    if len(MX[k]) == 1 and cand not in dones:
      single = cand
      break
  assert single is not None
  MX[k] = {single}
  dones.add(single)
  for k in MX:
    if single in MX[k] and len(MX[k]) != 1:
      MX[k].discard(single)
  done = True

R = [next(iter(MX[k])) for k in sorted(MX.keys())]

print(','.join(R))

