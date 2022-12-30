#!/usr/bin/env python3

L = open('7.in').read()
ALL = [(x[1], x[7]) for x in [l.split(' ') for l in L.splitlines()]]
FLAT = sorted({x for y in ALL for x in y})

def preq(c):
  return sorted({bef for bef,aft in ALL if aft == c})

def ready(cc, done):
  return all([c in done for c in cc])

res = ''
while len(res) < len(FLAT):
  for x in FLAT:
    if x not in res and ready(preq(x), res):
      res += x
      break
print(res)

seconds = 0
STEP = 60
S = [None] * 5
A = [None] * 5
res = ''
while len(res) < len(FLAT):
  finish = set()
  for w,s in enumerate(S):
    if s is not None:
      S[w] = s - 1
      if S[w] < 1:
        S[w] = None
        res += A[w]
        A[w] = None
  for x in FLAT:
    if x not in res and x not in A and ready(preq(x), res):
      for w,s in enumerate(S):
        if s is None:
          assert A[w] is None
          A[w] = x
          S[w] = STEP + FLAT.index(x) + 1
          break
  seconds += 1
print(seconds - 1)

