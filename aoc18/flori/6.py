#!/usr/bin/env python3

from collections import Counter

L = open('6.in').read()
A = [(int(a), int(b)) for a,b in [l.split(', ') for l in L.splitlines()]]

xx = [x for x,_ in A]
yy = [y for _,y in A]
minx, miny = min(xx), min(yy)
maxx, maxy = max(xx), max(yy)

# part 1
B = {}
for y in range(miny, maxy+1):
  for x in range(minx, maxx+1):
    res = Counter({(xa,ya): abs(x-xa) + abs(y-ya) for xa,ya in A})
    mc = res.most_common()
    if mc[-1][1] < mc[-2][1]:
      if mc[-1][0] not in B:
        B[mc[-1][0]] = []
      B[mc[-1][0]].append((x,y))
mx = -1
for (x,y),v in B.items():
  if x > minx and x < maxx and y > miny and y < maxy:
    mx = max(mx, len(v))
print(mx)

# part 2
sm = 0
for y in range(miny, maxy+1):
  for x in range(minx, maxx+1):
    if sum(abs(x-xa) + abs(y-ya) for xa,ya in A) < 10_000:
      sm += 1
print(sm)

