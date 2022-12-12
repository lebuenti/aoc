#!/usr/bin/env python3

from collections import deque

L = open('12.in').read().splitlines()

for part in (1,2):
  starts = []
  for y in range(len(L)):
    if 'E' in L[y]:
      target = L[y].index('E'), y, ord('z')
    if part == 1:
      if 'S' in L[y]:
        starts.append((L[y].index('S'), y, ord('a')))
    else:
      for x in range(len(L[y])):
        if L[y][x] == 'a':
          starts.append((x,y,ord('a')))
  assert target is not None

  founds = []
  for start in starts:
    seen = []
    Q = deque([([],start)])
    while Q:
      path,(x,y,z) = Q.popleft()
      if (x,y) in seen:
        continue
      seen.append((x,y))
      if (x,y,z) == target:
        founds.append([*path, (x,y,z)])
        continue
      for nx,ny in [
        (x+1,y),
        (x-1,y),
        (x,y+1),
        (x,y-1),
      ]:
        if nx < 0 or ny < 0 or nx >= len(L[y]) or ny >= len(L):
          continue
        n = L[ny][nx]
        nz = target[2] if n == 'E' else ord(n)
        if nz - z <= 1:
          Q.append(([*path, (x,y,z)], (nx, ny, nz)))

    if len(starts) == 1:
      print(min([len(f)-1 for f in founds]))

  if len(starts) > 1:
    if founds:
      print(min([len(f)-1 for f in founds]))

