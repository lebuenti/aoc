#!/usr/bin/env python3

from collections import deque

with open('22.in', 'r') as f:
  sp = f.read().split('\n\n')
  p1 = deque([int(n) for n in sp[0].splitlines()[1:]])
  p2 = deque([int(n) for n in sp[1].splitlines()[1:]])

def rec(rnd, game, p1, p2, one, ret=False):
  global DP

  mem = [[*p1],[*p2]]
  if str(mem) in DP:
    return DP[str(mem)]

  hist1 = []
  hist2 = []

  while p1 and p2:
    if one:
      c1, c2 = p1.popleft(), p2.popleft()
      if c1 > c2:
        p1.extend([c1,c2])
      elif c1 < c2:
        p2.extend([c2,c1])
    else:
      if list(p1) in hist1 and list(p2) in hist2 and hist2.index(list(p2)) == hist1.index(list(p1)):
        DP[str(mem)] = 1
        return DP[str(mem)]
        break
      hist1.append([*p1])
      hist2.append([*p2])
      c1, c2 = p1.popleft(), p2.popleft()
      if len(p1) >= c1 and len(p2) >= c2:
        winner = rec(1, game+1, deque([*p1][:c1]), deque([*p2][:c2]), one)  # sub-game
        if winner == 1:
          p1.extend([c1,c2])
        else:
          p2.extend([c2,c1])
      else:
        if c1 > c2:
          p1.extend([c1,c2])
        elif c1 < c2:
          p2.extend([c2,c1])
        
    rnd += 1

  if ret:
    return p1,p2

  DP[str(mem)] = 1 if p1 else 2
  return DP[str(mem)]

for one in (True, False):
  DP = {}
  res = rec(1, 1, deque([*p1]), deque([*p2]), one, ret=True)
  cards = (res[0] if res[0] else res[1])
  prod = 0
  factors = list(range(len(cards), 0, -1))
  for i in range(len(cards)):
    prod += cards[i] * factors[i]

  print(prod)

