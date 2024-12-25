#!/usr/bin/env python3

with open('10.in', 'r') as f:
  G = [[int(g) for g in l] for l in f.read().strip().splitlines()]

D = []
TH = [(x,y) for y in range(len(G)) for x in range(len(G[y])) if G[y][x] == 0]
S = [(th, []) for th in TH]
while S:
  (x,y), pp = S.pop()
  if G[y][x] == 9:
    D.append([*pp, (x,y)])
    continue
  for nx,ny in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]:
    if nx < 0 or ny < 0 or ny >= len(G) or nx >= len(G[ny]):
      continue
    if G[ny][nx] == G[y][x]+1:
      S.append(((nx,ny), [*pp, (x,y)]))

print(len({(d[0], d[-1]) for d in D}))
print(len(D))

