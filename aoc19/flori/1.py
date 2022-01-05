#!/usr/bin/env python3

with open('1.in', 'r') as f:
  ll = list(map(int, f.read().splitlines()))

f = 0
for m in ll:
  f += m // 3 - 2

print(f)

f = 0
for m in ll:
  tt = [m // 3 - 2]
  while 1:
    t = tt[-1] // 3 - 2
    if t <= 0:
      break
    tt.append(t)
  f += sum(tt)

print(f)

