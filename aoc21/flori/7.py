#!/usr/bin/env python

from math import inf


def triang(n):
  num = 0
  for k in range(n+1):
    num += k
  return num


with open('7.in', 'r') as f:
  ll = [int(i) for i in f.read().splitlines()[0].split(',')]

  DP = {}
  mx, mn = max(ll), min(ll)
  diff = +inf

  for i in range(mn, mx+1):
    cdiff = 0
    for l in ll:
      ldiff = abs(l-i)
      if ldiff not in DP:
        DP[ldiff] = triang(ldiff)
      cdiff += DP[ldiff]
    if cdiff < diff:
      diff = cdiff

  print(diff)

