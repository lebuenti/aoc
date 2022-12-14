#!/usr/bin/env python3

from collections import deque

ll = open('22.in').read().splitlines()

T = 10006

for l in ll:
  if l == "deal into new stack":
    # in-place
    print(S[100])
    S.reverse()
    print(S[100])
  elif l.startswith("cut "):
    # in-place
    cut = int(l.split(' ')[1])
    for _ in range(abs(cut)):
      if cut > 0:
        S.append(S.popleft())
      else:
        S.appendleft(S.pop())
  elif l.startswith("deal with increment "):
    # inst
    N = int(l.split(' ')[-1])
    lenS = len(S)
    nS = deque([None for _ in range(lenS)])
    pos = 0
    while S:
      assert nS[pos % lenS] is None
      nS[pos % lenS] = S.popleft()
      pos += N
    S = nS
    assert all([s is not None for s in S])

print(S.index(2019))

