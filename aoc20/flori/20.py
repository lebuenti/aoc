#!/usr/bin/env python3

from copy import deepcopy

with open ('20.in', 'r') as f:
  tiles = f.read().split('\n\n')

T = {}
for tile in tiles:
  ll = tile.splitlines()
  T[int(ll[0].split(' ')[-1][:-1])] = ll[1:]

def truncate(PIC, T):
  fy = fx = None
  for y in range(len(PIC)):
    for x in range(len(PIC[y])):
      if PIC[y][x] is not None:
        fy,fx = y,x
        break
    if fy is not None:
      break
  leng = int(len(T)**.5)
  return [j[fx:fx+leng] for j in PIC[fy:fy+leng]]

def hflip(t):
  return [x[::-1] for x in t]

def vflip(t):
  return [x for x in t[::-1]]

def rot(t, times):
  assert 0 < times < 4
  assert len(t) == len(t[0])
  N = len(t)
  _t = [[c for c in x] for x in t]
  for i in range(times):
    for x in range(0, N//2):
      for y in range(x, N-x-1):
        temp = _t[x][y]
        _t[x][y] = _t[y][N-1-x]
        _t[y][N-1-x] = _t[N-1-x][N-1-y]
        _t[N-1-x][N-1-y] = _t[N-1-y][x]
        _t[N-1-y][x] = temp
  return [''.join(x) for x in _t]

def xedge(t, side):
  assert side == 0 or side == -1
  return [t[y][side] for y in range(len(t))]

def yedge(t, side):
  assert side == 0 or side == -1
  return t[side]

def done(PIC, T):
  return sum([x is not None for y in PIC for x in y]) == len(T)

def permute(t):
  yield t
  yield hflip(t)
  yield vflip(t)
  yield hflip(vflip(t))
  yield rot(t, 1)
  yield rot(t, 2)
  yield rot(t, 3)
  yield hflip(rot(t, 1))
  yield hflip(rot(t, 2))
  yield hflip(rot(t, 3))
  yield vflip(rot(t, 1))
  yield vflip(rot(t, 2))
  yield vflip(rot(t, 3))
  yield hflip(vflip(rot(t, 1)))
  yield hflip(vflip(rot(t, 2)))
  yield hflip(vflip(rot(t, 3)))


def attempt(PIC, T):
  if done(PIC, T):
    return PIC

  # epically just the flattened ids
  USED = [None if k is None else k[0] for y in PIC for k in y if k is not None]

  for y in range(len(PIC)):
    for x in range(len(PIC[y])):
      if PIC[y][x] is None:
        continue
      adj = [PIC[y-1][x], PIC[y][x+1], PIC[y+1][x], PIC[y][x-1]]
      if adj.count(None) == 0:
        continue
      t1 = PIC[y][x][1]
      for ident,t in T.items():
        if ident == PIC[y][x][0]:
          continue
        if ident in USED:
          continue
        cands = set()
        for perm in permute(t):
          if adj[0] is None and yedge(perm, -1) == yedge(t1, 0):  # top
            cands.add((y-1,x))
          elif adj[1] is None and xedge(t1, -1) == xedge(perm, 0):  # right
            cands.add((y,x+1))
          elif adj[2] is None and yedge(t1, -1) == yedge(perm, 0):  # bottom
            cands.add((y+1,x))
          elif adj[3] is None and xedge(perm, -1) == xedge(t1, 0):  # left
            cands.add((y,x-1))

          for y,x in cands:
            _PIC = deepcopy(PIC)
            _PIC[y][x] = (ident,perm)
            res = attempt(_PIC, T)
            if res:
              return res

  return None

PIC = [[None]*int(len(T)) for _ in range(len(T))]
init_tile = next(iter(T.items()))
PIC[len(T)//2][len(T)//2] = init_tile
res = attempt(PIC, T)
trunc = truncate(res, T)
print(trunc[0][0][0] * trunc[-1][-1][0] * trunc[0][-1][0] * trunc[-1][0][0])

IMG = []
for y in range(len(trunc)):
  for i in range(1, len(trunc[0][0][1])-1):
    IMG.append('')
    for x in range(len(trunc[y])):
      IMG[-1] += trunc[y][x][1][i][1:-1]

indic = [0, 5, 6, 11, 12, 17, 18, 19]
M = '#'

for perm in permute(IMG):
  monsterized = False
  MONSTER = [*perm]
  for y in range(1, len(perm)-1):
    for x in range(0, len(perm[y])-(indic[-1])):
      monster = []
      cand=True
      for idx in indic:
        monster.append((y,x+idx))
        if perm[y][x+idx] != M:
          cand=False
          break
      if cand:
        monster.append((y-1,x+18))
        if perm[y-1][x+18] == M:
          for idx in range(x+1, x+18, 3):
            monster.append((y+1,idx))
            if perm[y+1][idx] != M:
              cand=False
              break
        else:
          cand=False
        if cand:
          for y,x in monster:
            MONSTER[y] = MONSTER[y][:x]+'O'+MONSTER[y][x+1:]
            monsterized=True

  if monsterized:
    print([y for k in MONSTER for y in k].count('#'))
    break

