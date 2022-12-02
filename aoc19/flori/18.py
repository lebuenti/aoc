#!/usr/bin/env python3

from collections import deque
from math import inf
import heapq

G = open('18.in', 'r').read().strip().splitlines()
root = None
K = {}
for y in range(len(G)):
  for x in range(len(G[y])):
    if G[y][x] == '@':
      assert root is None
      root = x,y
      # remove @ from grid
      G[y] = G[y][:x] + '.' + G[y][x+1:]
    if G[y][x].isalpha() and G[y][x].islower():
      K[G[y][x]] = (x,y)

# all unidirectional key and @ to key edges
M = {'@': {k: None for k in K.keys()}}
keys = sorted(list(K.keys()))
for i in range(len(keys)):
  M[keys[i]] = {}
  for k in range(i+1, len(keys)):
    M[keys[i]][keys[k]] = None

def neighs(x,y,coll=list(K.keys())):
  nn = []
  for c in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    try:
      g = G[c[1]][c[0]]
    except IndexError:
      continue
    if g == '.':
      nn.append(c)
    elif g.isalpha():
      if g.islower():
        nn.append(c)
      elif g.lower() in coll:
        nn.append(c)
  return nn

# bfs to find all keys
for f,tx in M.items():
  if f == keys[-1]:
    # already found everything toward last letter
    continue
  for t in tx.keys():
    start = root if f == '@' else K[f]
    Q = deque([(set(),set(),[],start)])
    while Q:
      seen,doors,path,(x,y) = Q.popleft()
      g = G[y][x]
      seen = {(x,y), *seen}
      path = [*path,(x,y)]
      if g == t:
        M[f][t] = (len(path)-1, doors)
        if f != '@':
          M[t][f] = M[f][t]
        break
      else:
        if g.isalpha() and g.isupper():
          if f == '@':
            continue
          doors = {g.lower(), *doors}
        for n in neighs(x,y):
          if n not in seen:
            Q.append((seen,doors,path,n))

# remove edges from @ that lead nowhere
M['@'] = {k: v for k,v in M['@'].items() if v is not None}

def expand(n):
  key,keys = n
  if len(K) == len(keys):
    return [(0, target)]
  rett = []
  for v,(cost,doors) in M[key].items():
    if v in keys:
      continue
    if not doors.issubset(keys):
      continue
    rett.append((cost,(v,frozenset({*keys, v}))))
  return rett

src = ('@', frozenset())
# fictional zero cost target node added when all keys collected
target = ('YAY', frozenset())
seen = set()
G = {src: 0}
P = {}
Q = [(0, 0, src)]
# dijkstra expanding nodes on-demand
while Q:
  f,g,n = heapq.heappop(Q)
  if n in seen:
    continue
  if target == n:
    break
  for cost,v in expand(n):
    vg = g + cost
    if v not in G or vg < G[v]:
      P[v] = n
      G[v] = vg
      heapq.heappush(Q, (vg, vg, v))
print(G[target])

