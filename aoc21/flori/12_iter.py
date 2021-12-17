#!/usr/bin/env python

from collections import deque, Counter

with open('12.ex', 'r') as f:
  G = [l.split('-') for l in f.read().splitlines()]


def neigh(u):
  global G
  res = []
  for n in G:
    if n[0] == u:
      res.append(n[1])
    elif n[1] == u:
      res.append(n[0])
  return [r for r in res if r != 'start']


def do(part2):
  c = 0
  Q = deque([['start']])
  while Q:
    p = Q.popleft()
    u = p[-1]

    if u == 'end':
      c += 1
      #print('d', ','.join(p))
      continue
      
    for n in neigh(u):
      part2_cond = part2 and \
        (all([v<2 for k,v in Counter(p).items() if k.islower()]) \
        and n not in ('start', 'end')) 
      if n.isupper() or n not in p or part2_cond:
        nexp = [*p]
        nexp.append(n)
        Q.append(nexp)

  return c

for i in range(2):
  print(i+1, do(i==1))

