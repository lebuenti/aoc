#!/usr/bin/env python3

with open('1.in', 'r') as f:
  X = [[int(n) for n in l.split("   ")] for l in f.readlines()]
L, R = [sorted(list(x)) for x in zip(*X)]

print(sum(abs(l - R[i]) for i,l in enumerate(L)))
print(sum(l * len([r for r in R if r == l]) for i,l in enumerate(L)))

