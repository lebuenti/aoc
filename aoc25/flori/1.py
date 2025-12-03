#!/usr/bin/env python3

L, D = 100, 50
p1, p2 = 0, 0
for l in open('1.in', 'r').read().strip().splitlines():
  d, num = l[:1], int(l[1:])
  if d == 'L':
    sub = 100 if D == 0 else 0
    rot = ((L-D-sub)+num) // L
  else:
    rot = (D+num) // L
  p2 += rot
  D = (D+(-num if d == 'L' else num)) % L
  p1 += D == 0
print(p1, p2)

