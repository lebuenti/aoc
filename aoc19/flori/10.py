#!/usr/bin/env python3

from math import inf, copysign

r = open('10.in', 'r').read()
ll = r.strip().splitlines()

def getslope(x1, y1, x2, y2):
  dx = (x2-x1)
  if dx == 0:
    return -inf if y1 > y2 else +inf
  return (y2-y1)/dx


def signed(n):
  return copysign(1, n) < 0


def getinsight(ll, x, y):
  curr = []
  for y1 in range(len(ll)):
    for x1 in range(len(ll[y1])):
      if ll[y1][x1] != '#':
        continue
      if y1 == y and x1 == x:
        continue
      s = getslope(x, y, x1, y1)
      res = (x1,y1), signed(s), s, x1-x > 0
      eq = None
      for c in curr:
        if c[1:] == res[1:]:
          eq = c
          break
      if eq is None:
        curr.append(res)
      elif abs(res[0][0]-x)+abs(res[0][1]-y) < abs(eq[0][0]-x)+abs(eq[0][1]-y):
        curr.remove(eq)
        curr.append(res)
  return curr


X = insight = None
for y in range(len(ll)):
  for x in range(len(ll[y])):
    if ll[y][x] != '#':
      continue
    curr = getinsight(ll, x, y)
    if insight is None or len(insight) < len(curr):
      insight = curr
      X = x,y

print(len(insight))

END = 200
F = [*ll]
shot = 0
while 1:
  side1,side0 = [], []
  posinf, neginf = None, None
  for idx,ins in enumerate(insight):
    if ins[2] == -inf:
      neginf = ins
    elif ins[2] == +inf:
      posinf = ins
    elif ins[3] == True:
      side1.append(ins)
    elif ins[3] == False:
      side0.append(ins)
  comp = [v for v in [neginf, *sorted(side1, key=lambda x: x[2]), posinf, *sorted(side0, key=lambda x: x[2])] if v is not None]
  assert sorted(comp) == sorted(insight)

  if shot + len(comp) < END:
    for i,((x,y),*_) in enumerate(comp):
      F[y] = F[y][:x] + "." + F[y][x+1:]
    shot += len(comp)
  else:
    (x,y),*_ = comp[END-shot-1]
    print(x*100+y)
    break

  insight = getinsight(F, *X)

