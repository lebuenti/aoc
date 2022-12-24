#!/usr/bin/env python3

import heapq

L = open('24.in').read()
ll = L.splitlines()

start = 1, 0
target = (len(ll[-1])-2, len(ll)-1)
WALLS = set()
BLIZZ = set()
dirs = ('>', '<', '^', 'v')
mov = ((1,0), (-1,0), (0,-1), (0,1))
for y in range(len(ll)):
  for x in range(len(ll[y])):
    if ll[y][x] == '#':
      WALLS.add((x,y))
    elif ll[y][x] in dirs:
      BLIZZ.add((ll[y][x], (x,y)))
    elif ll[y][x] == '.':
      pass
    else:
      raise Exception(f"Unexpected char {ll[y][x]}")

# all blizzes move forward!
def tick(blizz):
  tickd = set()
  for d, (x,y) in blizz:
    xd, yd = mov[dirs.index(d)]
    nx, ny = x+xd, y+yd
    if nx >= len(ll[ny])-1:
      nx = 1
    elif ny >= len(ll)-1:
      ny = 1
    elif nx < 1:
      nx = len(ll[ny])-2
    elif ny < 1:
      ny = len(ll)-2
    assert nx > 0 and ny > 0 and nx < len(ll[ny])-1 and ny < len(ll)-1
    tickd.add((d, (nx,ny)))
  return frozenset(tickd)

# there are only n unique statess
ticks = [BLIZZ]
while (tickd := tick(ticks[-1])) not in ticks:
  ticks.append(tickd)
ticks = []

# we know all states, don't need directions no more
ticks2 = []
for tick in ticks:
  t = set()
  for _,pos in tick:
    t.add(pos)
  ticks2.append(frozenset(t))
ticks = ticks2

def expand(x, y, blizz):
  ret = []
  for pos in [
    (x,y),
    (x+1,y),
    (x,y+1),
    (x-1,y),
    (x,y-1)
  ]:
    nx,ny = pos
    if nx < 0 or ny < 0 or nx >= len(ll[y]) or ny >= len(ll):
      continue
    if pos not in blizz and pos not in WALLS:
      ret.append(pos)
  return ret

def thru(fr, to, blizz):
  seen = set()
  Q = [(0, (blizz, fr))]
  while Q:
    V = heapq.heappop(Q)
    steps, v = V
    if V in seen:
      continue
    seen.add(V)
    blizz, (x,y) = v
    if (x,y) == to:
      return steps
    steps += 1
    blizz += 1
    for pos in expand(x, y, ticks[blizz % len(ticks)]):
      heapq.heappush(Q, (steps, (blizz, pos)))

a = thru(start, target, 0)
print(a)
b = thru(target, start, a)
c = thru(start, target , a+b)
print(sum([a,b,c]))

