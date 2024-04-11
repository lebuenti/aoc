#!/usr/bin/env python3

from collections import defaultdict
from math import inf

L = open('5.in').read()
ll = L.splitlines()

R = defaultdict(lambda: defaultdict(list))
i = 2
while i < len(ll):
  if not ll[i].endswith("map:"):
    continue
  fr, _, to = ll[i][:-5].split('-')
  i += 1
  while i < len(ll) and ll[i] != "":
    start_dest, start_src, rng = [int(n) for n in ll[i].split(" ")]
    R[fr][to].append((start_src, start_dest, rng))
    i += 1
  i += 1
TO = {fr: list(to.keys())[0] for fr,to in R.items()}

res = +inf
S = [('seed', int(n)) for n in ll[0].split(": ")[1].split(" ")]
while S:
  t, x = S.pop()
  if t == 'location':
    res = min(x, res)
  else:
    for start_src, start_dest, rng in R[t][TO[t]]:
      if x in range(start_src, start_src + rng):
        S.append((TO[t], (x - start_src) + start_dest))
        break
    else:
      S.append((TO[t], x))
print(res)

