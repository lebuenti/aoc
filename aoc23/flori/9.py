#!/usr/bin/env python3

sm1 = sm2 = 0
for l in open('9.in').read().splitlines():
  X = [[int(n) for n in l.split(" ")]]
  while any(x != 0 for x in X[-1]):
    X.append([X[-1][i+1] - X[-1][i] for i in range(len(X[-1])-1)])
  for i in range(len(X)-2, -1, -1):
    X[i].append(X[i][-1] + X[i+1][-1])
    X[i] = [(X[i][0] - X[i+1][0])] + X[i]
  sm1 += X[0][-1]
  sm2 += X[0][0]
print(sm1)
print(sm2)

