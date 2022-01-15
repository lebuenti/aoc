#!/usr/bin/env python3

from collections import defaultdict

OPS = {
  "e":  (+1,  0, -1),
  "w":  (-1,  0, +1),
  "se": ( 0, +1, -1),
  "sw": (-1, +1,  0),
  "ne": (+1, -1,  0),
  "nw": ( 0, -1, +1)
}

with open('24.in', 'r') as f:
  ll = f.read().splitlines()

MX_LEN = max([len(l) for l in ll])
V = defaultdict(lambda: True)  # white being true sticks better

for inp in ll:
  q,r,s = 0,0,0
  idx = 0
  while idx < len(inp):
    if inp[idx] in ('e','w'):
      q,r,s = [n+d for n,d in zip((q,r,s), OPS[inp[idx]])]
    else:
      q,r,s = [n+d for n,d in zip((q,r,s), OPS[inp[idx:idx+2]])]
      idx += 1

    assert q+r+s == 0  # https://www.redblobgames.com/grids/hexagons/#coordinates-cube
    idx += 1

  V[q,r,s] = not V[q,r,s]  # flip

print(len(V)-sum(V.values()))

for day in range(1, 100+1):
  # for any tile that we know, get its neighbors
  _V = V.copy()
  for (q,r,s),white in V.items():
    for dq,dr,ds in OPS.values():
      _V[q+dq,r+dr,s+ds]
  V=_V

  flips = []
  for (q,r,s),white in V.copy().items():
    blacks = sum([int(not V[q+dq,r+dr,s+ds]) for dq,dr,ds in OPS.values()])

    if (white and blacks == 2) or \
        (not white and (blacks == 0 or blacks > 2)):
      flips.append((q,r,s))

  for flip in flips:
    V[flip] = not V[flip]

print(len(V)-sum(V.values()))

