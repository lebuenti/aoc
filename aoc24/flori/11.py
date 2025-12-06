#!/usr/bin/env python3

from collections import defaultdict

L = "0 7 6618216 26481 885 42 202642 8791"

S = defaultdict(int)
for l in L.split(" "):
  S[int(l)] = 1

G = {}
for i in range(75):
  upd = defaultdict(int)
  for k,v in S.items():
    if v < 1:
      continue
    upd[k] -= v
    if k not in G:
      if k == 0:
        G[k] = [1]
      elif (lens := len((s := str(k)))) % 2 == 0:
        G[k] = [int(s[0:lens//2]), int(s[lens//2:])]
      else:
        G[k] = [k * 2024]
    for n in G[k]:
      upd[n] += v
  for k,v in upd.items():
    S[k] += v
  if i+1 == 25 or i+1 == 75:
    print(sum(S.values()))

