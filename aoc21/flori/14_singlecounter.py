#!/usr/bin/env python

from collections import Counter

with open('14.in', 'r') as f:
  tpl, _, *rules = f.read().split('\n')
  rules = rules[:-1]

R = dict(r.split(' -> ') for r in rules)

CP = Counter()
for i in range(len(tpl)-1):
  CP[tpl[i]+tpl[i+1]] += 1


for i in range(40):
  _CP = Counter()
  for (a, b), c in CP.items():
    r = R[a+b]
    _CP[a+r] += c
    _CP[r+b] += c

  CP = _CP

  if i == 9 or i == 39:
    CC = Counter()
    for (a, b), c in CP.items():
      CC[a] += c
      CC[b] += c
    CC[tpl[0]] += 1
    CC[tpl[1]] += 1

    mc = CC.most_common()
    print(mc[0][1]//2 - mc[-1][1]//2)

