#!/usr/bin/env python3

G = open('11.in').read().splitlines()

blackholes = [set(), set()]
for x in range(len(G[0])-1, -1, -1):
  if [G[y][x] for y in range(len(G))].count('.') == len(G):
    blackholes[0].add(x)
for y in range(len(G)):
  if G[y].count('.') == len(G[y]):
    blackholes[1].add(y)

X = [(x,y) for y in range(len(G)) for x in range(len(G[y])) if G[y][x] == '#']

for fac in (1, 1_000_000-1):
  sm = 0
  for i in range(len(X)):
    for j in range(i+1, len(X)):
      bh_sum = [sum(sum(x == bh for bh in blackholes[k]) for x in range(*sorted([X[i][k], X[j][k]]))) for k in (0,1)]
      sm += abs(X[i][0] - X[j][0]) + abs(X[i][1] - X[j][1]) + sum(bh_sum) * fac
  print(sm)

