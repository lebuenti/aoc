#!/usr/bin/env python3

import re
from math import inf

L = open('22.in').read()
P = open('22sq.in').read().splitlines()
ll = L.split("\n\n")

GG = ll[0].splitlines()

# creating the map for part 1
J = {}
dirs = '>', 'v', '<', '^'
start1 = None
maxx, maxy = -inf, -inf
for y in range(len(GG)):
  for x in range(len(GG[y])):
    if GG[y][x] in ('.', '#'):
      J[(x,y)] = GG[y][x]
      if start1 is None and GG[y][x] == '.':
        start1 = (0, (x,y))
      maxx = max(maxx, x)
      maxy = max(maxy, y)

# creating the map for part 2
N = 50
G = {i: {} for i in range(1, 6+1)}
dirs = '>', 'v', '<', '^'
start2 = (2, 0, (0,0))
MAX_X = {i: -inf for i in range(1, 6+1)}
MIN_X = {i: +inf for i in range(1, 6+1)}
MAX_Y = {i: -inf for i in range(1, 6+1)}
MIN_Y = {i: +inf for i in range(1, 6+1)}
for y in range(len(GG)):
  for x in range(len(GG[y])):
    if GG[y][x] in ('.', '#'):
      plane = int(P[y][x])
      G[plane][(x,y)] = GG[y][x]
      MAX_X[plane] = max(MAX_X[plane], x)
      MIN_X[plane] = min(MIN_X[plane], x)
      MAX_Y[plane] = max(MAX_Y[plane], y)
      MIN_Y[plane] = min(MIN_Y[plane], y)
G2 = {}
for plane,g in G.items():
  G2[plane] = {}
  for (x,y),v in g.items():
    G2[plane][x-MIN_X[plane], y-MIN_Y[plane]] = v
G = G2

# wrapping around the edges of a cube semi-hardcoded
DEF = {  #  >              v              <              ^
  1: ((4, 2,  True), (3, 2, False), (2, 2, False), (6, 3, False)),
  2: ((1, 0, False), (3, 1, False), (5, 0,  True), (6, 0, False)),
  3: ((1, 3, False), (4, 1, False), (5, 1, False), (2, 3, False)),
  4: ((1, 2,  True), (6, 2, False), (5, 2, False), (3, 3, False)),
  5: ((4, 0, False), (6, 1, False), (2, 0,  True), (3, 0, False)),
  6: ((4, 3, False), (1, 1, False), (2, 1, False), (5, 3, False)),
}
CON = {}
for leaveplane, neighbors in DEF.items():
  CON[leaveplane] = {}
  for leaveside, (enterplane, enterside, reverse) in enumerate(neighbors):
    # leaveside: leaving the plane out this side
    if leaveside == 0:    # >
      leave = [(N-1, y) for y in range(N)]
    elif leaveside == 1:  # v
      leave = [(x, N-1) for x in range(N)]
    elif leaveside == 2:  # <
      leave = [(0, y) for y in range(N)]
    elif leaveside == 3:  # ^
      leave = [(x, 0) for x in range(N)]

    # enterside: entering the plane from this side
    if enterside == 0:    # >
      enter = [(0, y) for y in range(N)]
    elif enterside == 1:  # v
      enter = [(x, 0) for x in range(N)]
    elif enterside == 2:  # <
      enter = [(N-1, y) for y in range(N)]
    elif enterside == 3:  # ^
      enter = [(x, N-1) for x in range(N)]

    # potentially x or y reverses onto the new plane
    if reverse:
      enter.reverse()

    # knowing the current plane, facing dir and coordinate
    #  we can get new plane, facing dir and coordinate
    CON[leaveplane][leaveside] = \
      dict(zip(leave, [(enterplane, enterside, (ex,ey)) for ex,ey in enter]))

# creating the instructions
gos1 = [int(n) for n in re.split('[A-Z]', ll[1].strip())]
gos2 = ['R', *[n for n in re.split('[0-9]+', ll[1].strip()) if n != '']]
assert len(gos1) == len(gos2)
insts = list(zip(gos2,gos1))

# let's go
goin = [(+1,0), (0,+1), (-1,0), (0,-1)]
for part in (1,2):
  first = True
  path = [start1 if part == 1 else start2]
  for i,(d,n) in enumerate(insts):
    # update facing direction
    facing = path[-1][int(part == 2)]
    assert d == 'L' or d == 'R'
    if not first:
      if d == 'L':
        facing = (facing - 1) % len(dirs)
      elif d == 'R':
        facing = (facing + 1) % len(dirs)
    first = False

    for go in range(1, n+1):
      if part == 1:
        x,y = path[-1][1]
        xd, yd = goin[facing]
        xn, yn = x+xd, y+yd
        if (xn, yn) in J:
          if J[xn,yn] == '#':
            path.append((facing, (x,y)))
            break
          elif J[xn,yn] == '.':
            pos = xn, yn
            path.append((facing, (xn,yn)))
          else:
            raise Exception(f"{J[yn][xn]}")
        else:
          # gotta wrap
          if facing == 0:
            # moving right
            for x1 in range(xn):
              if (x1,yn) in J:
                xn = x1
                break
            else:
              raise Exception("couldn't wrap")
          elif facing == 1:
            # moving down
            for y1 in range(yn):
              if (xn,y1) in J:
                yn = y1
                break
            else:
              raise Exception("couldn't wrap")
          elif facing == 2:
            # moving left
            for x1 in range(maxx, -1, -1):
              if (x1,yn) in J:
                xn = x1
                break
            else:
              raise Exception("couldn't wrap")
          elif facing == 3:
            # moving up
            for y1 in range(maxy, -1, -1):
              if (xn,y1) in J:
                yn = y1
                break
            else:
              raise Exception("couldn't wrap")
          if J[xn,yn] == '#':
            path.append((facing, (x,y)))
            break
          elif J[xn,yn] == '.':
            path.append((facing, (xn,yn)))
      else:
        # moving into facing direction
        plane = path[-1][0]
        x,y = path[-1][2]
        xd, yd = goin[facing]
        xn, yn = x + xd, y + yd

        if (xn, yn) in G[plane]:
          # within the same plane
          if G[plane][xn,yn] == '#':
            path.append((plane, facing, (x,y)))
            break
          elif G[plane][xn,yn] == '.':
            path.append((plane, facing, (xn,yn)))
          else:
            raise Exception(f"same plane {G[plane][yn][xn]}")
        else:
          # wrapping around another plane
          a = CON[plane][facing][x,y]
          nplane, f, (xn,yn) = a
          if G[nplane][xn,yn] == '#':
            path.append((plane, facing, (x,y)))
            break
          elif G[nplane][xn,yn] == '.':
            path.append(a)
            facing = f
          else:
            raise Exception(f"wrap around {G[plane][yn][xn]}")

  if part == 1:
    f, (x,y) = path[-1]
    print(1000 * (y + 1) + 4 * (x + 1) + f)
  else:
    p, f, (x,y) = path[-1]
    print(1000 * (y + 1 + MIN_Y[p]) + 4 * (x + 1 + MIN_X[p]) + f)

