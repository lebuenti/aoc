#!/usr/bin/env python3

L = open('3.in').read().splitlines()

p1 = 0
for l in L:
  mx = -1
  for i in range(0, len(l)-1):
    for k in range(i+1, len(l)):
      mx = max([int(l[i] + l[k]), mx])
  p1 += mx
print(p1)

M = 12
p2 = 0
for l in L:
  C = ""
  p = 0
  buff = len(l)-M
  while len(C) < M:
    to = [int(n) for n in l[p:p+buff+1]]
    mx = max(to)
    C += str(mx)
    idx = to.index(mx)
    buff -= idx
    p = idx+p+1
  p2 += int(C)
print(p2)

