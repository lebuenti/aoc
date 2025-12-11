#!/usr/bin/env python3

from collections import Counter

F = open('7.in').read().splitlines()

C = Counter({(F[0].index("S"), 0): 1})
p1 = 0
for tick in range(len(F)-1):
  for bx,by in [*C.keys()]:
    if C[bx,by] == 0:
      continue
    nx, ny = bx, by+1
    if F[ny][nx] == "^":
      C[nx-1,ny] += C[bx,by]
      C[nx+1,ny] += C[bx,by]
      p1 += 1
    else:
      C[nx,ny] += C[bx,by]
    C[bx,by] = 0
print(p1)
print(C.total())

