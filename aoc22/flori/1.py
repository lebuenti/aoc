#!/usr/bin/env python3

ll = open('1.in', 'r').read().splitlines()
sums = []
c = 0
for l in ll:
  if l == "":
    sums.append(c)
    c = 0
  else:
    c += int(l)

res = sorted(sums)[::-1][:3]
print('part1:', res[0])
print('part2:', sum(res))

