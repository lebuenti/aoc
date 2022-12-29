#!/usr/bin/env python3

from collections import Counter

L = open('4.in').read()
ll = L.splitlines()

# sort
R = []
for l in ll:
  year,month,day = [int(n) for n in l[1:11].split('-')]
  hour,minute = [int(n) for n in l[12:17].split(':')]
  txt = l[19:]
  act = None
  if txt == 'falls asleep':
    act = 'sleep'
  elif txt == 'wakes up':
    act = 'wake'
  elif txt.startswith("Guard"):
    act = int(txt.split(' ')[1][1:])
  else:
    raise Exception(txt)
  R.append(((year,month,day,hour,minute), act))

# add minutes
G = {}
fr = to = active = None
for (*_,minute),act in sorted(R):
  if act == 'sleep':
    assert fr is None
    fr = minute
  elif act == 'wake':
    assert to is None
    assert fr is not None
    to = minute
    G[active].update({i: 1 for i in range(fr, to)})
    to = fr = None
  else:
    active = act
    if act not in G:
      G[act] = Counter()

# part 1
g = mc = None
mx = -1
for guard, mm in G.items():
  if mm.total() > mx:
    mx = mm.total()
    g = guard
    mc = mm.most_common(1)[0][0]
print(g * mc)

# part 2
arr = []
for guard, mm in G.items():
  if not mm:
    continue
  mc = mm.most_common(1)[0]
  arr.append((*mc[::-1], guard))
arr.sort()
print(arr[-1][-1] * arr[-1][1])

