#!/usr/bin/env python3

ll = open('1.in', 'r').read().splitlines()
mx = -1
rng = [None] * 3
tops = [-1] * 3
for i in range(len(tops)):
  c = 0
  cnt = 0
  for l in ll:
    if l == "":
      cnt += 1
      if c > mx and not(cnt in rng[:i]):
        mx = c
        rng[i] = cnt
      c = 0
    else:
      c += int(l)
  tops[i] = mx
  mx = -1

print('part1:', tops[0])
print('part2:', sum(tops))

