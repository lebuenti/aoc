#!/usr/bin/env python3

from collections import Counter, defaultdict
from math import prod

L = open('2.in').read()
ll = L.splitlines()

T = Counter({'red': 12, "green": 13, "blue": 14})
works = sm = 0
for l in ll:
  g, nn = l.split(": ")
  g = int(g.split(" ")[1])
  yes = True
  C = defaultdict(int)
  for n1 in nn.split("; "):
    c = Counter({v: int(k) for k,v in [tuple(n.split(" ")) for n in n1.split(", ")]})
    for ckey in c.keys():
      C[ckey] = max(c[ckey], C[ckey])
    for k,v in c.items():
      if T[k] < v:
        yes = False
        break
  works += g * yes
  sm += prod(C.values())

print(works)
print(sm)

