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
L = deque(json.loads(L))

G = {(0,0): "X"}
NESW = {"N": (0,-1), "E": (+1,0), "S": (0,+1), "W": (-1,0)}
Q = deque([((0,0), L.popleft(), L)])
seen = set()
while Q:
  (x,y), q, l = Q.popleft()
  if not isinstance(q, str):
    X = (x,y), q[0], deque([*q[1:], *l])
    Q.appendleft(X)
    continue

  if ((x,y), q, str(l)) in seen:
    continue
  seen.add(((x,y), q, str(l)))

  for d in q:
    nx,ny = x + NESW[d][0], y + NESW[d][1]
    if d == "E" or d == "W":
      G[nx,ny] = "|"
    elif d == "N" or d == "S":
      G[nx,ny] = "-"
    else:
      raise Exception(d)
    x,y = nx + NESW[d][0], ny + NESW[d][1]
    G[x,y] = '.'
    G[x-1,y-1] = '#'
    G[x+1,y+1] = '#'
    G[x-1,y+1] = '#'
    G[x+1,y-1] = '#'

  if len(l) == 0:
    continue

  if isinstance(l[0], str):
    N = (x,y), l[0], deque(list(l)[1:])
    Q.append(N)
  else:
    for n in l.popleft():
      N = (x,y), n, l
      Q.append(N)

K = {(0,0): 0}
Q = deque([(0, (0,0))])
while Q:
  dist, (x,y) = Q.popleft()
  for nx,ny in [(x+dx*2, y+dy*2) for dx,dy in NESW.values() if (x+dx,y+dy) in G and G[x+dx,y+dy] != '#']:
    cost = dist + 1
    if (nx,ny) not in K or cost < K[nx,ny]:
      assert G[nx,ny] == '.'
      K[nx,ny] = cost
      Q.append((cost, (nx,ny)))

print(max(K.values()))
print(len([k for k in K.values() if k >= 1000]))

