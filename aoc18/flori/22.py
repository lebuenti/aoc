#!/usr/bin/env python3

from functools import cache
import heapq

ll = open('22.in').read().splitlines()

D = int(ll[0].split(': ')[1])
T = tuple([int(n) for n in ll[1].split(': ')[1].split(',')])
D,T = 510, (10,10)


@cache
def c_gi(x,y):
  if (x,y) == (0,0) or (x,y) == T:
    return 0
  elif y == 0:
    return x * 16807
  elif x == 0:
    return y * 48271
  return c_el(x-1,y) * c_el(x,y-1)


def c_el(x,y):
  return (c_gi(x,y) + D) % 20183


def c_type(x,y):
  el_mod_3 = c_el(x,y) % 3
  if el_mod_3 == 0:
    return '.'
  if el_mod_3 == 1:
    return '='
  if el_mod_3 == 2:
    return '|'
  raise Exception(el_mod_3)

RISK = {'.': 0, '=': 1, '|': 2}
risk = 0
for y in range(T[1]+1):
  for x in range(T[0]+1):
    t = c_type(x,y)
    if t in RISK:
      risk += RISK[t]
print(risk)

TORCH, GEAR = 'torch', 'gear'


def tools(x, y=None):
  t = x if y is None else c_type(x,y)
  if t == '.':
    return (TORCH, GEAR)
  if t == '=':
    return (GEAR, 'neither')
  if t == '|':
    return (TORCH, 'neither')
  raise Exception(str((x,y)) + ' ' + t)


def neighs(tool, xy):
  x,y = xy
  nn = []
  for nt in tools(x,y):
    if nt != tool:
      # change tool
      nn.append((7, (nt, (x,y))))
  for nx, ny in [
    (x+1, y),
    (x, y+1),
    (x-1, y),
    (x, y-1),
  ]:
    if nx < 0 or ny < 0:
      continue
    if tool in tools(nx,ny):
      # change region
      nn.append((1, (tool, (nx, ny))))
  return nn

start = TORCH, (0,0)
end = TORCH, T
G = {start: 0}
Q = [(0, start)]
seen = set()
while Q:
  m, g = heapq.heappop(Q)
  if g in seen:
    continue
  seen.add(g)
  if g == end:
    break
  for cost, ng in neighs(*g):
    nm = m + cost
    if ng not in G or G[ng] > nm:
      G[ng] = nm
      heapq.heappush(Q, (nm, ng))
print(G[end])

