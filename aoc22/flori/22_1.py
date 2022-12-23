#!/usr/bin/env python3

import re
from math import inf

L = \
"""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
L = open('22.in').read()
ll = L.split("\n\n")

GG = ll[0].splitlines()

# creating the map
G = {}
dirs = '>', 'v', '<', '^'
path = []
minx,maxx = +inf, -inf
miny,maxy = +inf, -inf
for y in range(len(GG)):
  for x in range(len(GG[y])):
    if GG[y][x] in ('.', '#'):
      G[(x,y)] = GG[y][x]
      if len(path) == 0 and GG[y][x] == '.':
        path.append((0, (x,y)))
      minx = min(minx, x)
      miny = min(miny, y)
      maxx = max(maxx, x)
      maxy = max(maxy, y)

# creating the instructions
gos1 = [int(n) for n in re.split('[A-Z]', ll[1].strip())]
gos2 = ['R', *[n for n in re.split('[0-9]+', ll[1].strip()) if n != '']]
assert len(gos1) == len(gos2)
insts = list(zip(gos2,gos1))
for i in range(len(insts)):
  print(insts[i])


def nice():
  print()
  for y in range(0, maxy+1):
    for x in range(0, maxx+1):
      p = ' '
      for f,(xp,yp) in path[::-1]:
        if (x,y) == (xp,yp):
          p = dirs[f]
          break
      else:
        if (x,y) in G:
          p = G[x,y]
      print(p,end='')
    print()
    
nice()

# let's go
goin = [(+1,0), (0,+1), (-1,0), (0,-1)]
first = True
for d,n in insts:
  facing = path[-1][0]
  assert d == 'L' or d == 'R'
  if not first:
    if d == 'L':
      facing = (facing - 1) % len(dirs)
    elif d == 'R':
      facing = (facing + 1) % len(dirs)
  first = False
  for go in range(1, n+1):
    x,y = path[-1][1]
    xd, yd = goin[facing]
    xn, yn = x+xd, y+yd
    if (xn, yn) in G:
      if G[xn,yn] == '#':
        path.append((facing, (x,y)))
        break
      elif G[xn,yn] == '.':
        pos = xn, yn
        path.append((facing, (xn,yn)))
      else:
        raise Exception(f"{G[yn][xn]}")
    else:
      # gotta wrap
      if facing == 0:
        # moving right
        for x1 in range(xn):
          if (x1,yn) in G:
            xn = x1
            break
        else:
          raise Exception("couldn't wrap")
      elif facing == 1:
        # moving down
        for y1 in range(yn):
          if (xn,y1) in G:
            yn = y1
            break
        else:
          raise Exception("couldn't wrap")
      elif facing == 2:
        # moving left
        for x1 in range(maxx, -1, -1):
          if (x1,yn) in G:
            xn = x1
            break
        else:
          raise Exception("couldn't wrap")
      elif facing == 3:
        # moving up
        for y1 in range(maxy, -1, -1):
          if (xn,y1) in G:
            yn = y1
            break
        else:
          raise Exception("couldn't wrap")
      if G[xn,yn] == '#':
        path.append((facing, (x,y)))
        break
      elif G[xn,yn] == '.':
        path.append((facing, (xn,yn)))

nice()
f, (x,y) = path[-1]
print(1000 * (y+1) + 4 * (x+1) + f)

