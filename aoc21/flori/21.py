#!/usr/bin/env python3

from collections import Counter
from functools import cache

s = [0, 0]
p = [1,6]
WIN = 1000
D = 1

turn = 0
while s[0] < WIN and s[1] < WIN:
  t = turn%2
  dice = [(D+i-1)%100+1 for i in range(3)]
  p[t] = (p[t]+sum(dice)-1)%10+1
  D+=3
  s[t] += p[t]
  #print(f"Player {t+1} rolls {dice} and moves to space {p[t]} for a total score of {s[t]}.")
  turn +=1

print(min(s) * (D-1))

@cache
def game(p, s, t):
  mx = max(s)
  if mx >= 21:
    return (mx==s[0], mx==s[1])
  res = 0, 0
  for d1 in (1,2,3):
    for d2 in (1,2,3):
      for d3 in (1,2,3):
        np, ns = [*p], [*s]
        idx = int(not t)
        np[idx] = (np[idx]+d1+d2+d3-1)%10+1
        ns[idx] += np[idx]
        w1, w2 = game(tuple(np), tuple(ns), not t)
        res = res[0]+w1, res[1]+w2
  return res

print(max(game((1,6), (0,0), True)))

