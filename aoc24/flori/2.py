#!/usr/bin/env python3

with open('2.in', 'r') as f:
  X = [[int(n) for n in l.split(" ")] for l in f.readlines()]

sm1 = sm2 = 0
for y in X:
  for k in range(-1, len(y)):
    x = [*y]
    if k >= 0:
      x.pop(k)
    incr = decr = adj = True
    for i in range(len(x)-1):
      if incr and x[i] > x[i+1]:
        incr = False
      elif decr and x[i] < x[i+1]:
        decr = False
      if not incr and not decr:
        break
      diff = abs(x[i] - x[i+1])
      if not (diff >= 1 and diff <= 3):
        adj = False
        break
    if (incr or decr) and adj:
      sm2 += 1
      sm1 += k == -1
      break

print(sm1)
print(sm2)

