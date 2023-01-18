#!/usr/bin/env python3

from collections import deque
import json

L = open('20.in').read().strip()

L = ('[["' + L[1:-1] + '"]]') \
  .replace("(", '",[["') \
  .replace(")", '"]],"') \
  .replace("|", '"],["') \
  .replace('],]', ']]') \
  .replace(',,', ',')
# eval(L) causes SyntaxError: too many nested parentheses
#  somehow doesn't happen with json.loads(L)
L = deque(json.loads(L))

DOOR = set()
ROOM = set()
NESW = {"N": (0,-1), "E": (+1,0), "S": (0,+1), "W": (-1,0)}
Q = deque([((0,0), L.popleft(), L)])
seen = set()
while Q:
  (x,y), q, l = Q.popleft()
  if not isinstance(q, str):
    Q.appendleft(((x,y), q[0], deque([*q[1:], *l])))
    continue

  if ((x,y), q, str(l)) in seen:
    continue
  seen.add(((x,y), q, str(l)))

  for d in q:
    nx,ny = x + NESW[d][0], y + NESW[d][1]
    DOOR.add((nx,ny))
    x,y = nx + NESW[d][0], ny + NESW[d][1]
    ROOM.add((x,y))

  if len(l) == 0:
    continue

  if isinstance(l[0], str):
    Q.append(((x,y), l[0], deque(list(l)[1:])))
  else:
    for n in l.popleft():
      Q.append(((x,y), n, l))

K = {(0,0): 0}
Q = deque([(0, (0,0))])
while Q:
  dist, (x,y) = Q.popleft()
  for nx,ny in [(x+dx*2, y+dy*2) for dx,dy in NESW.values() if (x+dx,y+dy) in DOOR]:
    cost = dist + 1
    if (nx,ny) not in K or cost < K[nx,ny]:
      K[nx,ny] = cost
      Q.append((cost, (nx,ny)))

print(max(K.values()))
print(len([k for k in K.values() if k >= 1000]))

