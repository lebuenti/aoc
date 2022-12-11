#!/usr/bin/env python3

from collections import defaultdict

ll = open('7.in').read().splitlines()

MOST = 100000
AVAIL = 70000000
REQ = 30000000

def pathify(*x):
  return '/'.join(x)[1:] or '/'

D = defaultdict(list)
hist = []
for l in ll:
  x = l.split(' ')
  if x[0] == '$':
    if x[1] == 'cd':
      if x[2] == '..':
        hist.pop()
      else:
        hist.append(x[2])
    elif x[1] != 'ls':
      raise Exception(x[1])
  else:
    c = x[0], pathify(*hist,x[1])
    path = pathify(*hist)
    assert c not in D[path]
    D[path].append(c)

S = defaultdict(int)
Q = ['/']
while Q:
  d = Q.pop()
  assert d in D
  for a,b in D[d]:
    if a == 'dir':
      Q.append(b)
    else:
      S[d] += int(a)
  if d != '/':
    parents = ['/', *[sub for sub in d.split('/') if sub][:-1]][::-1]
    prev = S[d]
    for i,p in enumerate(parents):
      parent = pathify(*parents[i:][::-1])
      assert parent in D
      S[parent] += S[d]

print(sum([size for size in S.values() if size <= MOST]))

for s in sorted(S.values()):
  free = AVAIL - (S['/']-s)
  if free >= REQ:
    print(s)
    break

