#!/usr/bin/env python3

from itertools import product

L = open('12.in').read()
ll = L.splitlines()

OPL, DMG, NON = ".", "#", "?"
PROD = {i: list(product([OPL, DMG], repeat=i)) for i in range(1, max(l.count(NON) for l in ll)+1)}

sm = 0
for l in ll:
  springs, groups = l.split(" ")
  springs = [n for n in springs]
  groups = [int(n) for n in groups.split(",")]
  nons = [i for i in range(len(springs)) if springs[i] == NON]
  arr = 0
  for prod in PROD[len(nons)]:
    s = [*springs]
    for i, p in enumerate(prod):
      s[nons[i]] = p
    arr += [len(n) for n in ''.join(s).split(OPL) if n != ''] == groups
  sm += arr
print(sm)

