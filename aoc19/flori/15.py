#!/usr/bin/env python3

from intcode import IntCode
from collections import deque

def neighs(x,y):
  return [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]

def mvhist(hist):
  mvs = []
  for i in range(1, len(hist)):
    fx,fy = hist[i-1]
    tx,ty = hist[i]
    mvs.append(neighs(fx, fy).index((tx,ty)) + 1)
  return mvs

I = open('15.in', 'r').read()
walls = []
pp = []
root = (0,0)
oxy = None
Q = deque([([root], n) for n in neighs(*root)])
E = {root, *neighs(*root)}
while len(Q) > 0:
  hist,(x,y) = Q.pop()
  path = [*hist, (x,y)]
  ic = IntCode(I, mvhist(path))
  res = ic()
  res = res[-1]
  if res == 2:
    # done
    pp.append(path)
    oxy = x,y
    continue
  elif res == 0:
    # hit wall
    walls.append((x,y))
  elif res == 1:
    for n in neighs(x,y):
      if n not in E:
        E.add(n)
        Q.append((path, n))
  else:
    raise Exception(str(res) + ' is unknown')

print('part1:', min([len(IntCode(I, mvhist(p))()) for p in pp]))

exp = [oxy]
dur = 0
E = {oxy}
while len(exp) > 0:
  new = []
  for x,y in exp:
    for n in neighs(x,y):
      if n not in walls and n not in E:
        E.add(n)
        new.append(n)
  exp = new
  if len(new) > 0:
    dur += 1
print('part2:', dur)

