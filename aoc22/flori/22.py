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
P = open('22sq.in').read().splitlines()
ll = L.split("\n\n")

GG = ll[0].splitlines()
# creating the map
N = 50
G = {i: {} for i in range(1, 6+1)}
dirs = '>', 'v', '<', '^'
path = [(2, 0, (0,0))]
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
MATCH = {i: {} for i in range(1, 6+1)}
G2 = {}
for plane,g in G.items():
  G2[plane] = {}
  for (x,y),v in g.items():
    G2[plane][x-MIN_X[plane], y-MIN_Y[plane]] = v
    MATCH[plane][x-MIN_X[plane], y-MIN_Y[plane]] = x,y
G = G2

# walking around the edges of a cube semi-hardcoded
DEF = {  #    >                v                <                ^
  1: ((4, '<',  True), (3, '<', False), (2, '<', False), (6, '^', False)),
  2: ((1, '>', False), (3, 'v', False), (5, '>',  True), (6, '>', False)),
  3: ((1, '^', False), (4, 'v', False), (5, 'v', False), (2, '^', False)),
  4: ((1, '<',  True), (6, '<', False), (5, '<', False), (3, '^', False)),
  5: ((4, '>', False), (6, 'v', False), (2, '>',  True), (3, '>', False)),
  6: ((4, '^', False), (1, 'v', False), (2, 'v', False), (5, '^', False)),
}
CON = {}
for leaveplane, neighbors in DEF.items():
  CON[leaveplane] = {}
  for leaveside, (enterplane, enterside, reverse) in enumerate(neighbors):
    # leaveside: leaving the plane out this side
    if leaveside == 0:  # >
      leave = [(N-1, y) for y in range(N)]
    elif leaveside == 1:  # v
      leave = [(x, N-1) for x in range(N)]
    elif leaveside == 2:  # <
      leave = [(0, y) for y in range(N)]
    elif leaveside == 3:  # ^
      leave = [(x, 0) for x in range(N)]

    # enterside: entering the plane from this side
    if enterside == '>':  # > 0 
      enter = [(0, y) for y in range(N)]
    elif enterside == 'v':  # v 1
      enter = [(x, 0) for x in range(N)]
    elif enterside == '<':  # < 2
      enter = [(N-1, y) for y in range(N)]
    elif enterside == '^':  # ^ 3
      enter = [(x, N-1) for x in range(N)]

    # potentially x or y reverses onto the new plane
    if reverse:
      enter.reverse()

    # knowing the current plane, facing dir and coordinate
    #  we can get new plane, facing dir and coordinate
    CON[leaveplane][leaveside] = \
      dict(zip(leave, [(enterplane, dirs.index(enterside), (ex,ey)) for ex,ey in enter]))

# creating the instructions
gos1 = [int(n) for n in re.split('[A-Z]', ll[1].strip())]
gos2 = ['R', *[n for n in re.split('[0-9]+', ll[1].strip()) if n != '']]
assert len(gos1) == len(gos2)
insts = list(zip(gos2,gos1))
for i in range(len(insts)):
  print(''.join([str(insts[i][0]), str(insts[i][1])]), end=', ')

def nice(only_current_plane=False):
  p = ''
  for plane,g in G.items():
    if only_current_plane and path[-1][0] != plane:
      continue
    p += f"plane {plane} {path[-1]}\n"
    for y in range(N):
      for x in range(N):
        w = ' '
        for i,(pl,f,(xp,yp)) in enumerate(path[::-1]):
          if (x,y) == (xp,yp) and pl == plane:
            color = '\033[96m' if i > 0 else '\033[92m'
            w = f"\033[1m{color}{dirs[f]}\033[0m"
            break
        else:
          if (x,y) in g:
            w = g[x,y]
        p += w
      p += "\n"
  print(p)

nice(True)
input()

# let's go
goin = [(+1,0), (0,+1), (-1,0), (0,-1)]
first = True
for i,(d,n) in enumerate(insts):
  # update facing direction
  facing = path[-1][1]
  if 0:
    while (d := input("L or R: ").upper()) not in ('R', 'L', ''):
      pass
    if d == '':
      first = True
      d = 'L'
    n = 1
  assert d == 'L' or d == 'R'
  if not first:
    if d == 'L':
      facing = (facing - 1) % len(dirs)
    elif d == 'R':
      facing = (facing + 1) % len(dirs)
  first = False

  for go in range(1, n+1):
    # moving into facing direction 
    plane = path[-1][0]
    x,y = path[-1][2]
    xd, yd = goin[facing]
    xn, yn = x+xd, y+yd

    #if (xn, yn) in G[plane]:
    if xn < N and yn < N and xn >= 0 and yn >= 0:
      # within the same plane
      if G[plane][xn,yn] == '#':
        path.append((plane, facing, (x,y)))
        break
      elif G[plane][xn,yn] == '.':
        path.append((plane, facing, (xn,yn)))
      else:
        raise Exception(f"{G[plane][yn][xn]}")
    else:
      # wrapping around another plane
      a = CON[plane][facing][x,y]
      nplane, f, (xn,yn) = a
      #print(f"wrap to plane {nplane} facing {f} at {xn},{yn} {G[nplane][xn,yn]}")
      if G[nplane][xn,yn] == '#':
        path.append((plane, facing, (x,y)))
        break
      elif G[nplane][xn,yn] == '.':
        path.append(a)
        facing = f
      else:
        raise Exception(f"{G[plane][yn][xn]}")
    #nice(True)
    #print(f"now:{d}{n} next: {insts[i+1]}")
    #print(f"now:{d}{n}")
    #input()

#nice()
p, f, (x,y) = path[-1]

#nice()
print('result', 1000 * (y+1) + 4 * (x+1) + f)

row = y+1+MIN_Y[p]
col = x+1+MIN_X[p]
print(row,col)
print('result', 1000 * (row) + 4 * (col) + f)

x,y = MATCH[p][x,y]
row = y + 1
col = x + 1
print(row,col)
print('result', 1000 * (row) + 4 * (col) + f)

print(p,f,(x,y))
# 43095 is too low
# 106007 is too low
# 177103 is too high

"""
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
  for x1 in range(N, -1, -1):
    if (x1,yn) in G:
      xn = x1
      break
  else:
    raise Exception("couldn't wrap")
elif facing == 3:
  # moving up
  for y1 in range(N, -1, -1):
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
"""

