#!/usr/bin/env python3

from intcode import IntCode
from collections import deque

L = open('21.in').read()

def toic(ss):
  ret = ','.join([str(ord(s)) for s in ss])
  return [int(r) for r in (ret+",10").split(',')]

OPS = ['OR', 'AND', 'NOT']
REG = ['J', 'T']

for mode in ("WALK", "RUN"):
  OPTS = [OPS, None, REG]
  LOOK = ['A', 'B', 'C', 'D']
  if mode == 'RUN':
    LOOK = [*LOOK, 'E', 'F', 'G', 'H', 'I']
  OPTS[1] = [*LOOK, *REG]

  opts = []
  for i in range(len(OPTS[0])):
    for j in range(len(OPTS[1])):
      for k in range(len(OPTS[2])):
        opts.append((OPTS[0][i],OPTS[1][j],OPTS[2][k]))

  Q = deque([[o] for o in opts])
  while Q:
    proc = Q.popleft()
    curr = {p[1] for p in proc}
    if all(look in curr for look in LOOK):
      parsed = [x for y in [toic(' '.join(p)) for p in proc] for x in y]
      run = IntCode(L, [*parsed, *toic(mode)])()
      if run[-1] != 10:
        print(run[-1])
        break
    for n in opts:
      # next is just the same as last
      # overriding T without using T
      # reading T without having it written before
      if n != proc[-1] \
      and (not (proc[-1][-1] == 'T' and n[-1] == 'T' and n[-2] != 'T')) \
      and (n[1] != 'T' or 'T' in {p[-1] for p in proc if p == 'T'}):
        Q.append([*proc, n])

