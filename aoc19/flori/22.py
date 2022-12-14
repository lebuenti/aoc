#!/usr/bin/env python3

from collections import deque

ll = open('22.in').read().splitlines()

L = 10007
S = deque(list(range(0,L)))

for l in ll:
  if l == "deal into new stack":
    # in-place
    S.reverse()
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

# again without actually maintaining the stack
now = 2019
for l in ll:
  if l == "deal into new stack":
    now = L-1-now
  elif l.startswith("cut "):
    cut = int(l.split(' ')[1])
    if cut > 0:
      if cut >= now+1:
        now = L-1-(cut-(now+1))
      else:
        now = now-cut
    else:
      if now >= L-abs(cut):
        now = abs(cut)-(L-now)
      else:
        now = now-cut
  elif l.startswith("deal with increment "):
    N = int(l.split(' ')[-1])
    now = (now*N) % L
print(now)

# TODO part 2 is too hard

