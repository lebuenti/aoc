#!/usr/bin/env python3

from collections import defaultdict

ll = open('23.in').read().splitlines()

G = set()
for y in range(len(ll)):
  for x in range(len(ll[y])):
    if ll[y][x] == '#':
      G.add((x,y))

NSWE = [
  (( 0,-1), (( 0,-1), (+1,-1), (-1,-1))),  # no elves at N, NE, or NW then move N
  (( 0,+1), (( 0,+1), (+1,+1), (-1,+1))),  # no elves at S, SE, or SW then move S
  ((-1, 0), ((-1, 0), (-1,-1), (-1,+1))),  # no elves at W, NW, or SW then move W
  ((+1, 0), ((+1, 0), (+1,-1), (+1,+1))),  # no elves at E, NE, or SE then move E
]

k = 0
while 1:
  # proposals
  froms = []
  tos = []
  for x,y in G:
    if all([
      (x+1, y+1) not in G,
      (x-1, y-1) not in G,
      (x  , y+1) not in G,
      (x+1, y  ) not in G,
      (x  , y-1) not in G,
      (x-1, y  ) not in G,
      (x-1, y+1) not in G,
      (x+1, y-1) not in G,
    ]):
      continue
    for i in range(len(NSWE)):
      (nx,ny), diffs = NSWE[(k+i) % len(NSWE)]
      for xd,yd in diffs:
        if (x+xd,y+yd) in G:
          break
      else:
        froms.append((x,y))
        tos.append((x+nx, y+ny))
        break

  # move
  move = False
  assert len(froms) == len(tos)
  for fr,to in zip(froms, tos):
    if tos.count(to) == 1:
      G.remove(fr)
      G.add(to)
      move = True

  if k == 10:
    xx = [x for x,_ in G]
    yy = [y for _,y in G]
    maxx, minx = max(xx), min(xx)
    maxy, miny = max(yy), min(yy)
    print(sum(int((x,y) not in G) for y in range(miny, maxy+1) for x in range(minx, maxx+1)))

  if not move:
    print(k+1)
    exit()

  k += 1

