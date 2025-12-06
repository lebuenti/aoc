#!/usr/bin/env python3

S = [s.splitlines() for s in open('5.in').read().split("\n\n")]
R = [(int(s), int(e)) for s,e in [r.split("-") for r in S[0]]]

p1 = 0
for ing in [int(n) for n in S[1]]:
  p1 += any(ing in range(s, e+1) for s,e in R)
print(p1)

sse = sorted(R)
tot = max(e for _,e in sse) - sse[0][0]
mx = -1
for i in range(0, len(sse)-1):
  _,e1 = sse[i]
  mx = max([mx, e1])
  s2,_ = sse[i+1]
  if mx < s2:
    tot -= s2-mx-1
print(tot+1)

