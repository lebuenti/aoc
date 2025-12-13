#/usr/bin/env python3

from random import randrange
from math import inf

L = []
for f in open('10.in').read().splitlines():
  onoff, *oth = f.split(" ")
  onoff = tuple([n == "#" for n in onoff[1:-1]])
  togg = [tuple(map(int, c.split(","))) for c in [n.strip("(").strip(")") for n in oth[:-1]]]
  jolts = tuple(map(int, oth[-1][1:-1].split(",")))
  L.append((onoff, togg, jolts))

p1 = 0
for onoff, togg, _ in L:
  Q = [(0, tuple([False] * len(onoff)))]
  seen = set()
  mn = +inf
  while Q:
    cnt, state = Q.pop(0)
    if state in seen:
      continue
    seen.add(state)
    if cnt >= mn:
      continue
    if onoff == state:
      mn = cnt
      continue
    for tog in togg:
      nx_state = [*state]
      for btn in tog:
        nx_state[btn] = not nx_state[btn]
      Q.append((cnt+1, tuple(nx_state)))
  p1 += mn
print(p1)

p2 = 0
for _, togg, jolts in L:
  mn_cnt = +inf
  S = [(0, tuple([*jolts]))]
  while S:
    cnt, state = S.pop()
    if cnt >= mn_cnt:
      continue
    if all(n == +inf for n in state):
      mn_cnt = cnt
      continue
    idx = state.index(mn := min(state))
    for t in [tog for tog in togg if idx in tog]:
      nx_state = [*state]
      for n in t:
        # TODO error is that nx_state[n] could already be inf
        nx_state[n] -= mn
      assert nx_state[idx] == 0
      nx_state[idx] = +inf
      S.append((cnt+mn, tuple(nx_state)))
  p2 += mn_cnt
print(p2)

