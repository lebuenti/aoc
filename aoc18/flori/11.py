#!/usr/bin/env python3

SERIAL = int(open('11.in').read().strip())
N = 300

P = {}
MXP = -1
for y in range(N):
  for x in range(N):
    rack_id = x + 10
    P[x,y] = int(str(((rack_id * y) + SERIAL) * rack_id).rjust(3,'0')[-3]) - 5
    MXP = max(P[x,y], MXP)

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
    sm = P[x,y]
    for s in range(N):
      if sm > mx:
        mx = sm
        res = x, y, s+1
      if x+s+1 == N or y+s+1 == N:
        break
      prev = sm
      for hy in range(y, y+s+1):
        sm += P[x+s+1, hy]
      for hx in range(x, x+s+1):
        sm += P[hx, y+s+1]
      sm += P[x+s+1, y+s+1]
      if prev - sm > MXP * 10:
        # wild guess to improve performance
        break
print(f"{res[0]},{res[1]},{res[2]}")

