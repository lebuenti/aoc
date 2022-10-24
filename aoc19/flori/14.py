#!/usr/bin/env python3

from collections import defaultdict
from math import ceil

ll = open('14.in', 'r').read().splitlines()
rr = []
for l in ll:
  ft = l.split('=>')
  f = [(int(x[0]),x[1]) for x in [f1.strip().split(' ') for f1 in ft[0].split(',')]]
  mats = [x[1] for x in f]
  if 'ORE' in mats:
    assert len(mats) == 1
  tsp = ft[1].strip().split(' ')
  assert len(tsp) == 2  # reacts to one material only
  rr.append([f, (int(tsp[0]), tsp[1])])

def getore(fuel):
  surp = defaultdict(int)
  S = [(fuel, 'FUEL')]
  ore = 0
  while len(S):
    q,m = S.pop()
    qtmp = max(0, q - surp[m])
    surp[m] = max(0, surp[m] - q)
    q = qtmp
    if q == 0:
      continue
    if m == 'ORE':
      ore += q
    for ff,(tq,tm) in rr:
      if tm == m:
        runs = ceil(q / tq)
        surp[tm] = runs * tq - q
        S.extend([(fq*runs, fm) for fq,fm in ff])
  return ore
print('part1:', getore(1))

trillion = 1000000000000
lo, hi = 0, 1
while getore(hi) < trillion:
  lo = hi
  hi *= 2
while hi - lo > 1:
  fuel = (hi + lo) // 2
  ore = getore(fuel)
  if ore > trillion:
    hi = fuel
  elif ore < trillion:
    lo = fuel
print('part2:', lo)

