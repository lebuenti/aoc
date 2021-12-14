#!/usr/bin/env python

with open('12.in', 'r') as f:
  G = [l.split('-') for l in f.read().splitlines()]


def neigh(u, G):
  res = []
  for n in G:
    if n[0] == u:
      res.append(n[1])
    elif n[1] == u:
      res.append(n[0])
  return [r for r in res if r != 'start']


def do(u, smol):
  V[u] += u.lower() == u
  pp.append(u)

  if u == 'end':
    yield ','.join(pp)
  else:
    if u not in N:
      N[u] = neigh(u, G)
    for n in N[u]:
      if V[n] < 1+(n==smol):
        yield from do(n, smol)

  pp.pop()
  V[u] -= 1


for i in range(2):
  N, pp, V = {}, [], {n: 0 for n in {x for c in G for x in c}}
  if i == 0:
    print('1', len(list(do('start', '-1'))))
  if i == 1:
    aa = set()
    for n in {x for c in G for x in c if x.islower()}:
      aa.update(set(do('start', n)))
    print('2', len(aa))

