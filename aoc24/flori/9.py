#!/usr/bin/env python3

with open('9.in', 'r') as f:
  G = f.read().strip()

X, b, free = [], 0, False
for i in range(len(G)):
  if not free:
    X.extend([str(b)] * int(G[i]))
    b += 1
  else:
    X.extend(['.'] * int(G[i]))
  free = not free

J = [*X]
for i in range(len(J)-1, -1, -1):
  n = J.index(".")
  if n >= i:
    break
  J[n], J[i] = J[i], '.'
print(sum(i * int(v) for i,v in enumerate(J) if v != '.'))

Y = sorted(list({x for x in X if x != '.'}), key=int)[::-1]
for y in Y:
  ii = [i for i,v in enumerate(X) if v == y]
  f, t = min(ii), max(ii)+1
  s = -1
  for i,v in enumerate(X):
    if v == '.' and s == -1:
      s = i
    elif v != '.' and s != -1:
      if i-s >= t-f and s <= f:
        for k in range(t-f):
          X[s+k], X[f+k] = y, '.'
        break
      s = -1
print(sum(i * int(v) for i,v in enumerate(X) if v != '.'))

