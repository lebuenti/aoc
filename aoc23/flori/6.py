#!/usr/bin/env python3

T, D = [62, 64, 91, 90], [553, 1010, 1473, 1074]
for r in [
  (T, D),
  [[int(''.join(str(x) for x in X))] for X in (T, D)]
]:
  prod = 1
  for t, d in zip(*r):
    prod *= len([i for i in range(1, t) if i*(t-i) > d])
  print(prod)

