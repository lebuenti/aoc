#!/usr/bin/env python3

from collections import defaultdict

L = [int(n) for n in open('8.in').read().strip().split(' ')]

M = {}
N = set()
G = defaultdict(list, {})
sm = 0
nx = [], 0
while 1:
  path, sp = nx
  children, meta = L[sp], L[sp+1]
  if not children:
    # leaf
    metadata = L[sp+2:sp+2+meta]
    N.add(sp)
    M[sp] = metadata
    sm += sum(metadata)
    G[path[-1]].append((sp,sp+2+meta-1))
    nx = [*path[:-1]], path[-1]
  else:
    if len(G[sp]) == 0:
      nx = [*path, sp], sp+2
    elif len(G[sp]) < children:
      nx = [*path, sp], sorted(G[sp])[-1][1] + 1
    else:
      metadata = L[sorted(G[sp])[-1][1]+1:sorted(G[sp])[-1][1]+1+meta]
      M[sp] = metadata
      sm += sum(metadata)
      if sp == 0:
        print(sm)
        break
      G[path[-1]].append((sp, sorted(G[sp])[-1][1]+meta))
      nx = [*path[:-1]], path[-1]

sm = 0
D = {k: [v1[0] for v1 in v] for k,v in G.items()}
S = [0]
while S:
  sp = S.pop()
  if sp not in N:
    for m in M[sp]:
      if m <= len(D[sp]):
        S.append(D[sp][m-1])
  else:
    sm += sum(M[sp])
print(sm)

