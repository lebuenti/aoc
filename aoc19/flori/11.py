#!/usr/bin/env python3

from collections import defaultdict
from intcode import IntCode

r = open('11.in', 'r').read()
for part in (1,2):
  di = 1
  C = {}
  P = defaultdict(lambda: 0)
  X,Y = 0,0
  P[(X,Y)] = part == 2
  ic = IntCode(r, [])

  while not ic.done():
    assert len(ic.inputs) == 0
    ic.inputs = [P[(X,Y)]]
    c,t = ic()

    assert c == 0 or c == 1
    P[(X,Y)] = c

    if t == 1:
      di = (((di+1)-1)%4)+1
    elif t == 0:
      di = di-1 or 4
    else:
      assert False

    if di == 1:
      Y -= 1 
    elif di == 2:
      X += 1
    elif di == 3:
      Y += 1
    elif di == 4:
      X -= 1
    else:
      assert False

  if part == 1:
    print('part1:', len(P))
    continue

  maxx, minx = \
    max([x for x,y in P.keys()]), \
    min([x for x,y in P.keys()])
  maxy, miny = \
    max([y for x,y in P.keys()]), \
    min([y for x,y in P.keys()])
  print('part2:');
  for x in range(maxy+1):
    for y in range(maxx+1):
      print(P[(y-miny,x-minx)] or ' ', end='')
    print()

