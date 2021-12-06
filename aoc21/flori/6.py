#!/usr/bin/env python

with open('6.in', 'r') as f:
  S = [int(i) for i in f.read().splitlines()[0].split(',')]
  K = [0] * 9
  for i in range(9):
    K[i] = len([s for s in S if s == i])

  c = len(S)
  for d in range(256):
    p = K.pop(0)
    K.append(p)
    K[6] = p+K[6]
    c += p

  print(c)

