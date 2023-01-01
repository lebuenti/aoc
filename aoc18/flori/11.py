#!/usr/bin/env python3

SERIAL = 9810
N = 300

P = {}
for y in range(N):
  for x in range(N):
    rack_id = x + 10
    P[x,y] = int(str(((rack_id * y) + SERIAL) * rack_id).rjust(3,'0')[-3]) - 5

# part 1
mx = -1
res = None
for y in range(1, N-1):
  for x in range(1, N-1):
    sm = sum([
      P[x,y],
      P[x-1,y-1],
      P[x+1,y+1],
      P[x+1,y-1],
      P[x-1,y+1],
      P[x,y+1],
      P[x,y-1],
      P[x+1,y],
      P[x-1,y],
    ])
    if sm > mx:
      mx = sm
      res = x-1,y-1
print(f"{res[0]},{res[1]}")

# part 2
mx = -1
res = None
for y in range(N):
  for x in range(N):
    minx = maxx = x
    miny = maxy = y
    sm = P[x,y]
    for s in range(N):
      if sm > mx:
        mx = sm
        res = x, y, s+1
      if maxx+1 == N or maxy+1 == N:
        break
      for hy in range(miny, maxy+1):
        sm += P[maxx+1, hy]
      for hx in range(minx, maxx+1):
        sm += P[hx, maxy+1]
      maxx += 1
      maxy += 1
      sm += P[maxx, maxy]
print(f"{res[0]},{res[1]},{res[2]}")

