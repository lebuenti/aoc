#!/usr/bin/env python3

ll = open('18.in').read().splitlines()

TREE, YARD, OPEN = '|', '#', '.'

K = {}
for y in range(len(ll)):
  for x in range(len(ll[y])):
    K[x,y] = ll[y][x]

def hashK(K):
  return hash(tuple(sorted(K.items())))

acc = False
WOW = 1000000000
m = 0

hs = hashK(K)
prevs = set([hs])
M = {hs: m}

while m < WOW:
  N = K.copy()
  for y in range(len(ll)):
    for x in range(len(ll[y])):
      nyards, ntrees = 0, 0
      for n in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y-1), (x+1,y-1), (x-1,y+1)]:
        if n in K:
          if K[n] == TREE:
            ntrees += 1
          elif K[n] == YARD:
            nyards += 1
      if K[x,y] == OPEN:
        if ntrees >= 3:
          N[x,y] = TREE
      elif K[x,y] == TREE:
        if nyards >= 3:
          N[x,y] = YARD
      elif K[x,y] == YARD:
        if not (nyards >= 1 and ntrees >= 1):
          N[x,y] = OPEN
  m += 1
  K = N
  if m == 10:
    print(sum(v == TREE for v in K.values()) * sum(v == YARD for v in K.values()))
  if not acc:
    if (hs := hashK(K)) not in prevs:
      prevs.add(hs)
      M[hs] = m
    else:
      acc = True
      # from m on it repeats every (m - M[hs]) minutes
      m = WOW - (WOW - m) % (m - M[hs])

print(sum(v == TREE for v in K.values()) * sum(v == YARD for v in K.values()))

