#!/usr/bin/env python3

from intcode import IntCode
from itertools import permutations
from math import inf

with open('7.in', 'r') as f:
  r = f.read()

mx_prev = -inf
for perm in permutations((0,1,2,3,4)):
  prev = 0
  for amp in range(5):
    ic = IntCode(r, inputs=(perm[amp], prev))
    prev, *superf = ic()
    if superf:
      break
  mx_prev = max(mx_prev, prev)

print(mx_prev)

mx_prev = -inf
for perm in permutations((5,6,7,8,9)):
  ics = [IntCode(r, inputs=[p]) for p in perm]
  ics[0].inputs.append(0)
  while 1:
    for amp in range(5):
      ic = ics[amp]
      if ic.done():
        continue
      prev, *_ = ic()
      assert not _
      ics[(amp+1)%5].inputs.append(prev)
      if amp == 4 and ic.done():
        break
    if amp == 4 and ic.done():
      break
  mx_prev = max(mx_prev, prev)

print(mx_prev)

