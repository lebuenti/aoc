#!/usr/bin/env python3

from collections import defaultdict
from math import inf

LOC = 'location'
SEED = 'seed'

L = open('5.in').read()
ll = L.splitlines()

R = defaultdict(lambda: defaultdict(list))
i = 2
while i < len(ll):
  if not ll[i].endswith("map:"):
    continue
  fr, _, to = ll[i][:-5].split('-')
  i += 1
  while i < len(ll) and ll[i] != "":
    start_dest, start_src, rng = [int(n) for n in ll[i].split(" ")]
    R[fr][to].append((start_src, start_dest, rng))
    i += 1
  i += 1
TO = {fr: list(to.keys())[0] for fr,to in R.items()}


def mapit(X, t, D):
  for start_src, start_dest, rng in X[t][D[t]]:
    if x >= start_src and x < start_src + rng:
      return D[t], (x - start_src) + start_dest
  return D[t], x


res = +inf
S = [(SEED, int(n)) for n in ll[0].split(": ")[1].split(" ")]
while S:
  t, x = S.pop()
  if t == LOC:
    res = min(x, res)
  else:
    S.append(mapit(R, t, TO))
print(res)

seeds = [int(n) for n in ll[0].split(": ")[1].split(" ")]
seeds = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]

# TO and R are seed to location
# FR and F are location to seed
FR = {v: k for k,v in TO.items()}
F = {v: {k: [(x[1], x[0], x[2]) for x in R[k][v]]} for k,v in TO.items()}

S = [(LOC, 0, 0)]
while S:
  t, x, loc = S.pop()
  if t == SEED:
    for s_start, s_end in seeds:
      if x >= s_start and x <= s_end:
        print(loc)
        break
    else:
      S.append((LOC, loc+1, loc+1))
  else:
    S.append((*mapit(F, t, FR), loc))

