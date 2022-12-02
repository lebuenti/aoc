#!/usr/bin/env python3

AB = {'A': 'X', 'B': 'Y', 'C': 'Z'}
P = {"X": 1, "Y": 2, "Z": 3}
W = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
L = {v: k for k,v in W.items()}
ll = [tuple(l.split(" ")) for l in open('2.in').read().splitlines()]
DRAW, WIN = 3, 6

p1,p2 = 0,0
for a,b in ll:
  y = AB[a]

  # p1
  if b == y:
    p1 += DRAW
  elif W[b] == y:
    p1 += WIN
  p1 += P[b]

  #p2
  if b == 'X':
    p2 += P[W[y]]
  if b == 'Y':
    p2 += DRAW
    p2 += P[AB[a]]
  if b == 'Z':
    p2 += WIN
    p2 += P[L[y]]

print(p1)
print(p2)

