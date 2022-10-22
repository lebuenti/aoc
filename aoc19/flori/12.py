#!/usr/bin/env python3

from math import inf, lcm

ll = open('12.in', 'r').read().splitlines()

for part in (1,2):
  oo = [
    [[int(n.split('=')[-1]) for n in l[:-1].split(',')], [0,0,0]]
    for l in ll
  ]
  init = [*[[*o[0]] for o in oo]]

  reps = [None] * 3
  step = 0
  while step < 1000 if part == 1 else inf:
    for i in range(len(oo)):
      for i1 in range(len(oo)):
        if i == i1:
          continue
        for ax in range(3):
          comp = oo[i][0][ax] - oo[i1][0][ax]
          if comp > 0:
            oo[i][1][ax] -= 1
          elif comp < 0:
            oo[i][1][ax] += 1

    for o in oo:
      for ax in range(3):
        o[0][ax] += o[1][ax]

    step += 1
    if part == 2:
      for ax in range(len(reps)):
        if reps[ax] is not None:
          continue
        if all([o[1][ax] == 0 for o in oo]):
          if [o[0][ax] for o in oo] == [o[ax] for o in init]:
            reps[ax] = step
            if all(reps):
              print('part2:', lcm(*reps))
              quit()

  if part == 1:
    tot = 0
    for o in oo:
      tot += sum([abs(n) for n in o[0]]) * sum([abs(n) for n in o[1]])
    print('part1:', tot)

