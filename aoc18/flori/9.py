#!/usr/bin/env python3

from collections import deque

L = open('9.in').read().strip().split(' ')
END = int(L[-2])

for mul in (1, 100):
  P = [0] * int(L[0])
  F = deque([0])
  for n in range(1, END*mul+1):
    if n % 23 == 0:
      F.rotate(8)
      P[(n+1) % len(P)] += F.pop() + n
      F.rotate(-2)
    else:
      F.append(n)
      F.rotate(-1)
  print(max(P))

