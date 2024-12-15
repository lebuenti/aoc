#!/usr/bin/env python3

with open('7.in', 'r') as f:
  X = f.read().splitlines()

tot1 = tot2 = 0
for x in X:
  a,b = x.split(": ")
  a = int(a)
  bb = [int(n) for n in b.split(" ")]
  S = [(bb[0], 1, False)]
  hit_p1 = hit_p2 = False
  while S:
    sm, j, p2 = S.pop()
    if j == len(bb):
      if sm == a:
        if p2 is False:
          if not hit_p1:
            tot1 += a
            hit_p1 = True
        if not hit_p2:
          tot2 += a
          hit_p2 = True
        if hit_p1 and hit_p2:
          break
      continue
    if sm > a:
      continue
    for nx in [sm + bb[j], sm * bb[j]]:
      S.append((nx, j + 1, p2))
    S.append((int(str(sm) + str(bb[j])), j + 1, True))
print(tot1)
print(tot2)

