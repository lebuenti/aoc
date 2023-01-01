#!/usr/bin/env python3

import re

G = set()
PATTERN = "position=< *(-?[0-9]+), *(-?[0-9]+)> velocity=< *(-?[0-9]+), *(-?[0-9]+)>"
for l in open('10.in').read().splitlines():
  px,py,vx,vy = [int(n) for n in re.compile(PATTERN).match(l).groups()]
  G.add(((px,py),(vx,vy)))

s = 0
xd,yd = 100, 100
while xd > 70 or yd > 15:
  G2 = set()
  for (px,py),(vx,vy) in G:
    G2.add(((px+vx,py+vy),(vx,vy)))
  G = G2
  s += 1
  xy =  [(x,y) for (x,y),_ in G]
  xx = [x for x,_ in xy]
  yy = [y for _,y in xy]
  minx, miny = min(xx), min(yy)
  maxx, maxy = max(xx), max(yy)
  xd = maxx - minx
  yd = maxy - miny

for y in range(miny, maxy+1):
  for x in range(minx, maxx+1):
    p = ' '
    if (x,y) in xy:
      p = '#'
    print(p, end='')
  print()
print(s)

