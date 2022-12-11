#!/usr/bin/env python3

from collections import deque
import heapq
from math import inf

IDENT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
Lo = open('20.in', 'r').read()

def neighs(grid, x,y):
  nn = []
  for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    if nx < 0 or ny < 0 or nx > len(grid[y])-1 or ny > len(grid)-1:
      continue
    g = grid[ny][nx]
    if g != '#' and g != ' ':
      nn.append((nx,ny))
  return nn

for part in (1,2):
  L = Lo.splitlines()
  K = {}
  for y in range(len(L)):
    for x in range(len(L[y])):
      l = L[y][x]
      if not l.isalpha():
        continue
      for nx,ny in neighs(L, x,y):
        n = L[ny][nx]
        if n != '.':
          continue
        o = L[y+(y-ny)][x+(x-nx)]
        if y < ny or x < nx:
          conn = o+l
        elif x > nx or y > ny:
          conn = l+o
        ident = IDENT[len(K)]
        if conn == 'AA':
          start = ident
        elif conn == 'ZZ':
          target = ident
        K[ident] = (nx,ny), conn

  assert start is not None
  assert target is not None

  Kpos = {pos: (ident,ft) for ident,(pos,ft) in K.items()}

  G = []
  for y in range(2,len(L)-2):
    G.append([])
    for x in range(2,len(L[y])-2):
      if (x,y) in Kpos:
        G[-1].append(Kpos[(x,y)][0])
      else:
        if L[y][x].isalpha():
          G[-1].append(' ')
        else:
          G[-1].append(L[y][x])

  K = {ident: ((x-2,y-2),ft) for ident,((x,y),ft) in K.items()}
  Kpos = {pos: (ident,ft) for ident,(pos,ft) in K.items()}

  M = {}
  for ident,(pos,ft) in K.items():
    Q = deque([(frozenset(),pos)])
    while Q:
      seen,(x,y) = Q.popleft()
      if (x,y) in seen:
        continue
      seen = frozenset({*seen, (x,y)})
      if G[y][x] != start and G[y][x] != ident and G[y][x] in IDENT:
        if ident not in M:
          M[ident] = {}
        via = K[G[y][x]][1]
        cost = len(seen)
        if y == 0 or x == 0 or y == len(G)-1 or x == len(G[y])-1:
          dim = -1
        else:
          dim = +1
        if G[y][x] == target:
          M[ident][target] = cost-1,dim
        else:
          for ident1,(pos1,ft1) in K.items():
            if via == ft1 and G[y][x] != ident1:
              M[ident][ident1] = cost,dim
              break
          else:
            raise Exception()
        continue
      for n in neighs(G, x,y):
        Q.append((seen,n))

  def expand(lf):
    l,f = lf
    if part == 1:
      return [((-1, t), cost) for t,(cost,_) in M[f].items()]
    rett = []
    if f not in M:
      return rett
    for t,(cost,dim) in M[f].items():
      st = t == start or t == target
      add = False
      if l == 0:
        if dim > 0 or st:
          add = True
      elif not st:
        add = True
      if add:
        rett.append(((l+dim, t), cost))
    return rett

  # dijkstra lazy expanding nodes
  seen = set()
  G = {start: 0}
  P = {}
  Q = [(0, (0,start))]
  while Q:
    g,ln = heapq.heappop(Q)
    if ln in seen:
      continue
    seen.add(ln)
    if ln == (-1, target):
      break
    for (lv),cost in expand(ln):
      vg = g + cost
      if lv not in G or vg < G[lv]:
        P[lv] = ln
        G[lv] = vg
        heapq.heappush(Q, (vg, lv))
  print(G[-1,target])

