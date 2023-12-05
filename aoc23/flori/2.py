#!/usr/bin/env python3

from collections import Counter

L = open('2.in').read()
ll = L.splitlines()

T = Counter({'red': 12, "green": 13, "blue": 14})
works = 0
for l in ll:
  g, nn = l.split(": ")
  g = int(g.split(" ")[1])
  yes = True
  for n1 in nn.split("; "):
    c = Counter({v: int(k) for k,v in [tuple(n.split(" ")) for n in n1.split(", ")]})
    for k,v in c.items():
      if T[k] < v:
        yes = False
        break
    if not yes:
      break
  works += g * yes
print(works)

