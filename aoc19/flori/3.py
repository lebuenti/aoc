#!/usr/bin/env python3

from math import inf

with open('2.in', 'r') as f:
  r = f.read()
  ll = [[(s[0],int(s[1:])) for s in l.split(',')] for l in r.splitlines()]

S = 0,0
I = set()
V = set()  # x by y
P = []

for l in ll:
  flt = [v[0] for v in V for k in v]
  vv = set()
  s = S
  for di,dist in l:
    for i in range(1, dist+1):
      if di == 'R':
        nx = s[0]+i,s[1]
      elif di == 'L':
        nx = s[0]-i,s[1]
      elif di == 'U':
        nx = s[0],s[1]+i
      elif di == 'D':
        nx = s[0],s[1]-i
      vv.add(nx)
    s = nx
  P.append(list(vv))
  for v in vv:
    if v in V:
      I.add(v)
    else:
      V.add(v)

mn = +inf
for x,y in I:
  mn = min(abs(S[0]-x) + abs(S[1]-y), mn)

print(mn)

mn = +inf
for v1 in P:
  for v2 in P:
    if v1 == v2:
      continue
    for v11 in v1:
      if v11 in v2:
        mn = min(v1.index(v11) + v2.index(v11) + 2, mn)

print(mn)

