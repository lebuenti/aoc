#!/usr/bin/env python


def neigh(G, r, c, idx=False):
  coords = {
    (max(0,r-1), c),
    (min(len(G)-1,r+1), c),
    (r, max(0, c-1)),
    (r, min(len(G[r])-1, c+1)),
    (max(0,r-1), max(0,c-1)),
    (max(0,r-1), min(len(G[r])-1, c+1)),
    (min(len(G)-1,r+1), max(0,c-1)),
    (min(len(G)-1,r+1), min(len(G[r])-1,c+1)),
  }
  coords = [coo for coo in coords if coo != (r,c)]
  return coords if idx else [G[nr][nc] for nr,nc in coords]


with open('11.in', 'r') as f:
  ll = f.read().splitlines()


G = []
for l in ll:
  G.append([int(i) for i in [_ for _ in l]])

count = step = 0
while True:
  step += 1

  for r in range(len(G)):
    for c in range(len(G[r])):
      G[r][c] += 1

  f = []
  while True:
    bef = len(f)
    for r in range(len(G)):
      for c in range(len(G[r])):
        if G[r][c] > 9 and (r,c) not in f:
          f.append((r,c))
          for nr, nc in neigh(G, r, c, idx=True):
            if not (G[nr][nc] == 9 and (nr,nc) in f):
              G[nr][nc] += 1
    if bef == len(f):
      break

  count += len(f)
  for r, c in f:
    G[r][c] = 0
  f = []

  all_flash = True
  for r in range(len(G)):
    for c in range(len(G[r])):
      if G[r][c] != 0:
        all_flash = False
  
  if all_flash:
    print(step)
    break

