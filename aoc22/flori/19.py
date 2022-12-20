#!/usr/bin/env python3

import re
from collections import defaultdict

L = open('19.in').read()
ll = L.splitlines()

PATTERN = "Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore\. Each clay robot costs ([0-9]+) ore\. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay\. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian\."

ore = "ore"
clay = "clay"
obsidian = "obsidian"
geode = "geode"
mats = [ore, clay, obsidian, geode]
LOOKUP = {mat: i for i,mat in enumerate(mats)}

B = {}
for l in ll:
  blueprint, *costs = re.compile(PATTERN).match(l).groups()
  costs = [int(n) for n in costs]
  B[int(blueprint)] = {
    ore: defaultdict(int, {ore: costs[0]}),
    clay: defaultdict(int, {ore: costs[1]}),
    obsidian: defaultdict(int, {ore: costs[2], clay: costs[3]}),
    geode: defaultdict(int, {ore: costs[4], obsidian: costs[5]}),
  }

def spendings(b, D, REQ):
  prepare = []
  for mat in mats:
    if mat in REQ and REQ[mat] <= R[LOOKUP[mat]][1]:
      continue
    for req,n in b[mat].items():
      if n > D[LOOKUP[req]][1]:
        break
    else:
      if mat == geode:
        return [geode]
      prepare.append(mat)
  return prepare

for part in (1,2):
  MINUTES = 32 if part == 2 else 24

  mxes = []
  for k,b in B.items():
    if part == 2 and k not in (1,2,3):
      continue

    REQ = {mat: 0 for mat in mats if mat != geode}
    for v in b.values():
      for req, n in v.items():
        if req in REQ:
          REQ[req] = max(REQ[req], n)

    seen = set()
    S = [(1, tuple((m, 0) for m in mats), tuple((m, int(m == ore)) for m in mats))]
    mx = -1
    while S:
      V = S.pop()

      if V in seen:
        continue
      seen.add(V)

      m, D, R = V

      # collect
      Dcoll = tuple((mat, n + R[LOOKUP[mat]][1]) for mat,n in D)

      if m == MINUTES:
        mx = max(mx, Dcoll[LOOKUP[geode]][1])
        continue

      # triangular numbers
      mleft = MINUTES - m
      if ((mleft * (mleft + 1)) / 2) + mleft * R[LOOKUP[geode]][1] + Dcoll[LOOKUP[geode]][1] <= mx:
        continue

      S.append((m+1, Dcoll, R))
      for mat in spendings(b, D, REQ):
        S.append((
          m + 1,
          tuple((mat1, n - b[mat][mat1]) for mat1,n in Dcoll),
          tuple((mat1, n + int(mat == mat1)) for mat1,n in R),
        ))
    mxes.append(mx)

  if part == 1:
    print(sum((i + 1) * s for i,s in enumerate(mxes)))
  else:
    print(mxes[0] * mxes[1] * mxes[2])

