#!/usr/bin/env python3

from collections import Counter

with open('2.in', 'r') as f:
  ll = [i for i in f.readlines()]

tt = Counter({ 2: 0, 3: 0 })

for l in ll:
  tt[2] += 2 in Counter(l).values()
  tt[3] += 3 in Counter(l).values()

print('part1', tt[2] * tt[3])

for l in ll:
  for l1 in ll:
    if l1 == l:
      continue
    d = None
    fail = False
    for i in range(len(l)):
      if l[i] != l1[i]:
        if d is not None:
          fail = True
          break
        d = i
    if not fail:
      print('part2', ''.join([l[i] for i in range(len(l)) if i != d]))
      quit()

