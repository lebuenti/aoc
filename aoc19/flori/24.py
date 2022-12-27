#!/usr/bin/env python3

from math import inf

L = open('24.in').read()
ll = L.splitlines()

minx, maxx = +inf, -inf
miny, maxy = +inf, -inf
minz, maxz = 0, 0
K = set()
for y in range(len(ll)):
  for x in range(len(ll[y])):
    if x == 2 and y == 2:
      continue
    if ll[y][x] == '#':
      K.add((x,y,0))
      minx = min(minx, x)
      maxx = max(maxx, x)
      miny = min(miny, y)
      maxy = max(maxy, y)
  
for part in (1,2):
  kk = [{*K}]
  m = 1
  while 1:
    k = {*K}
    for z in (0,) if part == 1 else range(minz-1, maxz+1+1):
      for y in range(len(ll)):
        for x in range(len(ll[y])):
          if part == 2 and x == 2 and y == 2:
            continue
          c = 0
          for nx,ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if part == 2:
              if (nx,ny) == (2,2):
                if x == 1:
                  poss = ((0,ny1,z+1) for ny1 in range(5))
                elif x == 3:
                  poss = ((4,ny1,z+1) for ny1 in range(5))
                elif y == 1:
                  poss = ((nx1,0,z+1) for nx1 in range(5))
                elif y == 3:
                  poss = ((nx1,4,z+1) for nx1 in range(5))
                else:
                  raise Exception(f"{x},{y}")
                c += sum(pos in K for pos in poss)
              elif nx == -1:
                c += (1,2,z-1) in K
              elif nx >= len(ll[y]):
                c += (3,2,z-1) in K
              elif ny == -1:
                c += (2,1,z-1) in K
              elif ny >= len(ll):
                c += (2,3,z-1) in K
              else:
                c += (nx,ny,z) in K
            else:
              c += (nx,ny,z) in K
          if (x,y,z) in K:
            if c != 1:
              k.remove((x,y,z))
          else:
            if c == 1 or c == 2:
              k.add((x,y,z))
    K = k
    if part == 1 and k in kk:
      print(sum(2 ** (5 * y + x + 1 - 1) for x,y,_ in k))
      break
    elif part == 2 and m == 200:
      print(len(K))
      break
    kk.append(k)
    zz = [coord[2] for coord in K]
    minz, maxz = min(zz), max(zz)
    m += 1

