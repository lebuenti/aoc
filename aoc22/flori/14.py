#!/usr/bin/env python3

from itertools import zip_longest

L = open('14.in').read()
ll = L.splitlines()

rocks = set()
for l in ll:
  trails = l.split(' -> ')
  for i in range(len(trails)-1):
    (fx,fy),(tx,ty) = \
      [int(n) for n in trails[i].split(',')], \
      [int(n) for n in trails[i+1].split(',')]
    assert fx == tx or fy == ty
    if fy == ty:
      rev = int(fx > tx)
      rocks.update(zip_longest(range(fx, tx+1-rev-rev, -1 if rev else 1), [], fillvalue=ty))
    elif fx == tx:
      rev = int(fy > ty)
      rocks.update(zip_longest([], range(fy, ty+1-rev-rev,  -1 if rev else 1), fillvalue=tx))

SAND = 500,0
maxy = max(y for _,y in rocks)
floory = maxy+2

def pour(part):
  sands = set()
  while 1:
    s = SAND
    while s is not None:
      sx,sy = s
      for n in [(sx,sy+1), (sx-1,sy+1), (sx+1,sy+1)]:
        if part == 1 and s[1] > maxy:
          return len(sands)
        if n not in sands and n not in rocks and s[1] < floory-1:
          s = n
          break
      else:
        sands.add(s)
        if part == 2 and s == SAND:
          return len(sands)
        s = None

for part in (1,2):
  print(pour(part))

