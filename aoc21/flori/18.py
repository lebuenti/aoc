#!/usr/bin/env python

from collections import deque
from math import ceil

with open('18.in', 'r') as f:
  ll = f.read().splitlines()


class Fish:
  def __init__(self, x):
    if isinstance(x, str):
      self.pair = eval(x)
    else:
      self.pair = x

  def explode(self):
    L, R, Q = 3, [], deque([([0], self.pair[0]), ([1], self.pair[1])])
    while Q:
      indic, (l, r) = Q.popleft()
      apps = [None, None]
      if isinstance(l, list):
        apps[0] = l
      if isinstance(r, list):
        apps[1] = r
      if len(indic) == L:
        for i in range(len(apps)):
          if apps[i] is not None and \
              isinstance(apps[i][0], int) and isinstance(apps[i][1], int):
            R.append(([*indic, i], apps[i]))
            break
        continue
      for i in range(len(apps)):
        if apps[i] is not None:
          Q.append(([*indic, i], apps[i]))
      
    if len(R) < 1:
      return None

    r = R[0]
    p = self.pair[r[0][0]]
    for idx in r[0][1:]:
      p = p[idx]

    # change ref, str, reset ref
    rem = [*r[1]]
    p[0], p[1] = 'x', 'y'
    pstr = str(p).replace(" ", "")
    selfstr = str(self)
    p[0], p[1] = rem[0], rem[1]

    fidx = selfstr.find(pstr)
    bef, aft = selfstr[:fidx], selfstr[fidx+len(pstr):]

    idx = len(bef)-1
    while idx > 0:
      num = ''
      while bef[idx].isdigit():
        num = bef[idx] + num
        idx -= 1
      if num != '':
        upd = str(int(num) + int(p[0]))
        bef = bef[:-(len(bef)-idx)+1] + upd + bef[-(len(bef)-idx)+1+len(num):]
        break
      idx -= 1

    idx = 0
    while idx < len(aft):
      num = ''
      while aft[idx].isdigit():
        num += aft[idx]
        idx += 1
      if num != '':
        upd = str(int(num) + int(p[1]))
        aft = aft[:idx-len(num)] + upd + aft[idx:]
        break
      idx += 1

    return Fish(bef + '0' + aft)

  def split(self):
    selfstr = str(self)
    nums = selfstr.replace("[", "").replace("]", "").split(",")
    ii = [i.strip() for i in nums if i.isdigit() and int(i) >= 10]
    if len(ii) < 1:
      return None
    i = ii[0]
    fidx = selfstr.find(str(i))
    upd = str(Fish([int(i)//2, ceil(int(i)/2)]))
    return Fish(selfstr[:fidx] + upd + selfstr[fidx+len(str(i)):])

  def magnitude(self):
    selfstr = str(self)
    while selfstr.count('[') > 1:
      for i in range(len(selfstr)-1):
        if selfstr[i] == '[':
          idx = i+1
          l = ''
          while selfstr[idx].isdigit():
            l += selfstr[idx]
            idx += 1
          if selfstr[idx] == ',' and selfstr[idx+1].isdigit():
            r = ''
            idx += 1
            while selfstr[idx].isdigit():
              r += selfstr[idx]
              idx += 1
            selfstr = selfstr[:i] + str(3*int(l) + 2*int(r)) + selfstr[idx+1:]
            break

    l,r = [int(n) for n in eval(selfstr)]
    return 3*l + 2*r

  def __getitem__(self, idx):
    return self.pair[idx]

  def __add__(self, other):
    return Fish([self.pair, other])

  def __repr__(self):
    return str(self.pair).replace(" ", "")


def run(f):
  while True:
    cf = f.explode()
    if cf is not None:
      f = cf
    else:
      cf = f.split()
      if cf is not None:
        f = cf
      else:
        break

  return f

f = Fish(ll[0])
for i in range(len(ll)-1):
  f = run(f + Fish(ll[i+1]))
print('1', f.magnitude())

mx = -1
for i in range(len(ll)):
  fi = Fish(ll[i])
  for k in range(len(ll)):
    if i != k:
      fk = Fish(ll[k])
      mx = max(run(fi + fk).magnitude(), mx)

print('2', mx)
    
