#!/usr/bin/env python3

L = [[int(n) for n in r] for r in open('8.in').read().splitlines()]

coords = [(x,y) for y in range(len(L)) for x in range(len(L[y]))]
DIR = [
  {(x,y): [L[y][x1] for x1 in range(len(L[y]))][:x][::-1] for x,y in coords},
  {(x,y): [L[y][x1] for x1 in range(len(L[y]))][x+1:] for x,y in coords},
  {(x,y): [L[y1][x] for y1 in range(len(L))][:y][::-1] for x,y in coords},
  {(x,y): [L[y1][x] for y1 in range(len(L))][y+1:] for x,y in coords},
]
LOOK = {xy: [di[xy] for di in DIR] for xy in coords}

sm = len(L) * 2 + len(L[0]) * 2 - 4
for y in range(1,len(L)-1):
  for x in range(1,len(L[y])-1):
    for i, di in enumerate(LOOK[(x,y)]):
      if all([l1 < L[y][x] for l1 in (di if i > 1 else di[::-1])]):
        sm += 1
        break
print(sm)

scenic = -1
for x,y in coords:
  l = L[y][x]
  prod = 1
  for di in LOOK[(x,y)]:
    sm = 0
    for n in di:
      sm += 1
      if n >= l:
        break
    prod *= sm
  scenic = max(scenic, prod)
print(scenic)

