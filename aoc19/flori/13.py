#!/usr/bin/env python3

from intcode import IntCode
from collections import defaultdict

r = open('13.in', 'r').read()

def prettyp(G):
  mxx, mxy = 0, 0
  for x,y,_ in G:
    mxx = max(x, mxx)
    mxy = max(y, mxy)
  for y in range(mxy+1):
    for x in range(mxx+1):
      for gx,gy,ident in G:
        if gx == x and gy == y:
          print(ident or ' ', end='')
    print()

ic = IntCode(r)
out = ic()
assert ic.done()
B = {}
for i in range(0, len(out), 3):
  x,y,ident = out[i:i+3]
  if ident == 2:
    B[x,y] = ident
print('part1:', len(B))

score = None
G = []
init = False
ic = IntCode(','.join(['2', *r.split(',')[1:]]))
while 2 in [g[2] for g in G] or not init:
  out = ic()
  for i in range(0, len(out), 3):
    x,y,ident = out[i:i+3]
    if x == -1 and y == 0:
      score = ident 
    else:
      if not init:
        G.append([x,y,ident])
      else:
        for i in range(len(G)):
          gx,gy,_ = G[i]
          if gx == x and gy == y:
            G[i][2] = ident
            break
  init = True
  #prettyp(G)
  #print()
  #input()
  ball = [g[0] for g in G if g[2] == 4][0]
  paddle = [g[0] for g in G if g[2] == 3][0]
  ic.inputs = [-1 if paddle > ball else 0 if paddle == ball else +1]
print('part2:', score)


