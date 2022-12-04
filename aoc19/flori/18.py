#!/usr/bin/env python3

from collections import deque
import heapq

L = open('18.in', 'r').read().strip()

for step in (1,2):
  G = L.splitlines()
  roots = None
  K = {}
  for y in range(len(G)):
    for x in range(len(G[y])):
      if G[y][x] == '@' and roots is None:
        if step == 1:
          roots = [(x,y)]
          G[y] = G[y][:x] + '.' + G[y][x+1:]
        else:
          # clockwise
          roots = [(x-1,y-1),(x+1,y-1),(x+1,y+1),(x-1,y+1)]
          G[y-1] = G[y-1][:x-1] + '.#.' + G[y-1][x+2:]
          G[y] = G[y][:x-1] + '###' + G[y][x+2:]
          G[y+1] = G[y+1][:x-1] + '.#.' + G[y+1][x+2:]
      if G[y][x].isalpha() and G[y][x].islower():
        K[G[y][x]] = (x,y)

  # all unidirectional key and root to key edges
  keys = sorted(list(K.keys()))
  M = {str(i): {k: None for k in keys} for i in range(len(roots))}
  for i in range(len(keys)):
    M[keys[i]] = {}
    for k in range(i+1, len(keys)):
      M[keys[i]][keys[k]] = None

  def neighs(x,y):
    nn = []
    for c in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
      try:
        g = G[c[1]][c[0]]
      except IndexError:
        continue
      if g != '#':
        nn.append(c)
      #if g == '.' or g.isalpha():
      #  nn.append(c)
    return nn

  # bfs to find all keys
  for f,tx in M.items():
    if f == keys[-1]:
      # already found everything toward last letter
      continue
    for t in tx.keys():
      start = roots[int(f)] if f.isdigit() else K[f]
      Q = deque([(set(),set(),[],start)])
      while Q:
        seen,doors,path,(x,y) = Q.popleft()
        g = G[y][x]
        seen = {(x,y), *seen}
        path = [*path,(x,y)]
        if g == t:
          M[f][t] = (len(path)-1, doors)
          if not f.isdigit():
            M[t][f] = M[f][t]
          break
        else:
          if g.isalpha() and g.isupper():
            doors = {g.lower(), *doors}
          for n in neighs(x,y):
            if n not in seen:
              Q.append((seen,doors,path,n))

  # remove edges that lead nowhere
  for f,_ in M.items():
    M[f] = {k: v for k,v in M[f].items() if v is not None}

  # fictional zero cost target node added when all keys collected
  target = ('YAY', frozenset())

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

  # dijkstra lazy expanding nodes
  goal = None
  src = (tuple([str(roots.index(d)) for d in roots]), frozenset())
  seen = set()
  G = {src: 0}
  P = {}
  Q = [(0, 0, src)]
  while Q:
    f,g,n = heapq.heappop(Q)
    if n in seen:
      continue
    seen.add(n)
    if target[0] in n[0]:
      goal = n
      break
    for i in range(len(n[0])):
      for cost,v in expand((n[0][i], n[1])):
        vg = g + cost
          
        nl = list(n[0])
        nl[i] = v[0]
        v = (tuple(nl), v[1])

        if v not in G or vg < G[v]:
          P[v] = n
          G[v] = vg
          heapq.heappush(Q, (vg, vg, v))
  print(G[goal])

