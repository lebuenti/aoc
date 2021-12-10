#!/usr/bin/env python

def neigh(G, r, c, idx=False):
  coords = {
    (max(0,r-1), c), (min(len(G)-1,r+1), c),
    (r, max(0, c-1)), (r, min(len(G[r])-1, c+1)),
  }
  coords = [coo for coo in coords if coo != (r,c)]
  return coords if idx else [G[nr][nc] for nr,nc in coords]


def j1():
  lvl = 0

  for r in range(len(G)):
    for c in range(len(G[r])):
      nn = neigh(G, r, c)
      if len([n for n in nn if n > G[r][c]]) == len(nn):
        lvl += 1 + G[r][c]

  return lvl


def flow(G, r, c):
  vis = []
  s = [(r,c)]
  c = 0
  while len(s) > 0:
    nr, nc = s.pop()
    if G[nr][nc] != 9 and (nr, nc) not in vis:
      c += 1
      s.extend(neigh(G, nr, nc, idx=True))
    vis.append((nr,nc))
  return c


def j2():
  baisins = []
  for r in range(len(G)):
    for c in range(len(G[r])):
      nn = neigh(G, r, c)
      nn_idx = neigh(G, r, c, idx=True)
      if len([n for n in nn if n > G[r][c]]) == len(nn):
        baisins.append(flow(G, r, c))
  return sorted(baisins, reverse=True)[:3]


with open('9.in', 'r') as f:
  ll = f.read().splitlines()

G = []
for l in ll:
  G.append([int(i) for i in [_ for _ in l]])


print('1', j1())

resj2 = j2()
print('2', resj2[0] * resj2[1] * resj2[2])

