#!/usr/bin/env python3

import re
from collections import deque
from math import inf

L = open('16.in').read()
ll = L.splitlines()

PATTERN = "Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.+)"
G = {}
for l in ll:
  valve, rate, nn = re.compile(PATTERN).match(l).groups()
  tunnels = nn.split(', ')
  G[valve] = int(rate),tunnels

pressurized = frozenset({valve for valve,(rate,_) in G.items() if rate > 0})
maxrelease = sum(G[v][0] for v in pressurized)

M = {}
V = ['AA', *pressurized]
for i in range(len(V)-1):
  iv = V[i]
  for j in range(i+1, len(V)):
    jv = V[j]
    seen = set()
    Q = deque([(0,iv)])
    while Q:
      minutes,v = Q.popleft()
      if v in seen:
        continue
      seen.add(v)
      if v == jv:
        if iv not in M:
          M[iv] = {}
        assert jv not in M[iv]
        M[iv][jv] = minutes
        if iv != 'AA':
          if jv not in M:
            M[jv] = {}
          assert iv not in M[jv]
          M[jv][iv] = minutes
        break
      for nv in G[v][1]:
        if nv != iv:
          Q.append((minutes+1, nv))

for part in (1,2):
  END = 26 if part == 2 else 30
  mx = -1
  seen = set()
  S = [(1, frozenset(), 0, ('AA', 0), ('AA', 0))]
  while S:
    V = S.pop()
    m, releasing, released, (va,ma), (vb,mb) = V

    if V in seen:
      continue
    seen.add(V)

    # processing what comes first by minute
    mbef = m
    if ma <= mb:
      m = m + ma
      v = va
      vm = ma
      vo = vb
      mo = mb
    else:
      m = m + mb
      v = vb
      vm = mb
      vo = va
      mo = ma

    if m > END:
      released += (END - mbef) * sum(G[v1][0] for v1 in releasing)
      mx = max(mx, released)
      continue

    released += sum(G[v1][0] for v1 in releasing) * (vm - 1)

    if v != 'AA':
      releasing = frozenset({*releasing, v})
    released += sum(G[v1][0] for v1 in releasing)

    if releasing == pressurized:
      # all pressurized valves open
      mx = max(mx, released + maxrelease * (END - m))
      continue

    if mx >= released + maxrelease * (END - m):
      # perfect outcome couldn't exceed current mx
      continue

    if m == END:
      mx = max(mx, released)
      continue

    if part == 1:
      for na in M[va]:
        if na in releasing:
          continue
        S.append((
          m,
          releasing,
          released,
          (na, M[va][na] + 1),
          (vb, +inf)
        ))
    else:
      add = False
      for vn in M[v]:
        if vn in releasing or vn == vo:
          continue
        add = True
        S.append((
          m,
          releasing,
          released,
          (vn, M[v][vn] + 1),
          (vo, mo - vm),
        ))
      if not add:
        # all valves open, finish off
        S.append((
          m,
          releasing,
          released,
          ('AA', +inf),
          (vo, mo - vm),
        ))

  print(mx)

