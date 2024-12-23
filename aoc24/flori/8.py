#!/usr/bin/env python3

from collections import defaultdict

with open('8.in', 'r') as f:
  G = f.read().splitlines()

K = defaultdict(list)
for y in range(len(G)):
  for x in range(len(G[y])):
    if G[y][x] != '.':
      K[G[y][x]].append((x,y))

A, B = [], []
for a, aa in K.items():
  for j in range(len(aa)-1):
    xj,yj = aa[j]
    for k in range(j+1, len(aa)):
      xk,yk = aa[k]
      if (xj,yj) == (xk,yk):
        continue
      for m in range(1, len(G) * len(G[0])):
        dx = (xj-xk)*m
        dy = (yj-yk)*m
        Alenbef = len(A)
        if (nx := xj+dx) >= 0 and nx < len(G[0]) \
          and (ny := yj+dy) >= 0 and ny < len(G):
          A.append((nx,ny))
          if m == 1:
            B.append((nx,ny))
        if (nx := xk-dx) >= 0 and nx < len(G[0]) \
          and (ny := yk-dy) >= 0 and ny < len(G):
          A.append((nx,ny))
          if m == 1:
            B.append((nx,ny))
        if len(A) == Alenbef:
          break
      A.append(aa[j])
      A.append(aa[k])

print(len(set(B)))
print(len(set(A)))

