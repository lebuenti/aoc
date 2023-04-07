#!/usr/bin/env python3

with open('1.in', 'r') as f:
  ll = [int(i) for i in f.readlines()]

for p in (1,2):
  freq = 0

  if p == 1:
    for l in ll:
      i = int(l)
      freq += i
    print('part1:', freq)

  if p == 2:
    D = {freq: True}
    while True:
      for l in ll:
        i = int(l)
        freq += i
        done = freq in D
        if done:
          print('part2:', freq)
          break
        D[freq] = True
      if done:
        break

