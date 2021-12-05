#!/usr/bin/env python

import numpy as np 

MAX = 990

with open('5.in', 'r') as f:
  ll = [l.split(' -> ') for l in f.read().splitlines()]
  inp = [([int(i) for i in l[0].split(',')], [int(i) for i in l[1].split(',')]) for l in ll]

  F = np.zeros((MAX+1,MAX+1), dtype=int)
  
  for [x1, y1], [x2, y2] in inp:
    if x1 == x2:
      x = x1
      if y1 < y2:
        for y in range(y1, y2+1):
          F[y][x] += 1
      else:
        for y in range(y1, y2-1, -1):
          F[y][x] += 1
    elif y1 == y2:
      y = y1
      if x1 < x2:
        for x in range(x1, x2+1):
          F[y][x] += 1
      else:
        for x in range(x1, x2-1, -1):
          F[y][x] += 1
    else:
      if y1 > y2:
        y = range(y1, y2-1, -1)
      else:
        y = range(y1, y2+1)
        print([y1 for y1 in y])
      if x1 < x2:
        for i, x in enumerate(range(x1, x2+1)):
          F[y[i]][x] += 1
      else:
        for i, x in enumerate(range(x1, x2-1, -1)):
          F[y[i]][x] += 1

print(np.count_nonzero(F >= 2)) 

