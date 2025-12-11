#!/usr/bin/env python3

from math import inf, sqrt, prod
from collections import defaultdict

F = open('8.in').read().splitlines()
F = [(int(x), int(y), int(z)) for x,y,z in [n.split(",") for n in F]]
D = defaultdict(dict)
for i in range(len(F)-1):
  x,y,z = F[i]
  mn, mn_it = +inf, None
  for k in range(i+1, len(F)):
    x1,y1,z1 = F[k]
    D[F[i]][F[k]] = sqrt((x-x1)**2 + (y-y1)**2 + (z-z1)**2)

dft = sorted([(d,f,t) for f,tt in D.items() for t,d in tt.items()])
C = [[f] for f in F]
for j, (d,f,t) in enumerate(dft):
  fi, ti = None, None
  for i in range(len(C)):
    if f in C[i]:
      assert fi is None
      fi = i
    if t in C[i]:
      assert ti is None
      ti = i
    if fi is not None and ti is not None:
      break
  else:
    assert False
  if fi != ti:
    C[ti].extend(C.pop(fi))
    if len(C) == 1:
      print(f[0] * t[0])
      break
  if j == 1000:
    print(prod(len(c) for c in sorted(C, key=len)[-3:]))

