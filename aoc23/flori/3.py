#!/usr/bin/env python3

import re
from math import prod

L = open('3.in').read()
ll = L.splitlines()

ff = set()
g_sm = 0
for y in range(len(ll)):
  for x in range(len(ll[y])):
    if ll[y][x].isdigit() or ll[y][x] == ".":
      continue
    gear = set()
    for x1,y1 in [
      (x-1,y-1),
      (x-1,y+0),
      (x-1,y+1),
      (x+1,y-1),
      (x+1,y+0),
      (x+1,y+1),
      (x+0,y+1),
      (x+0,y-1),
    ]:
      if x1 < 0 or y1 < 0 or y1 > len(ll) or x1 > len(ll[y1]) \
      or not ll[y1][x1].isdigit():
        continue
      e = re.search(r'^\d*', ll[y1][x1:])
      s = re.search(r'^\d*', ll[y1][x1::-1][1:])
      end = x1 + e.end()
      start = end - len(s.group()[::-1] + e.group())
      ff.add((y1, (start,end)))
      gear.add((y1, (start,end)))
    if ll[y][x] == "*" and len(gear) == 2:
      g_sm += prod(int(ll[y][s:e]) for y, (s,e) in gear)

print(sum(int(ll[y][s:e]) for y, (s,e) in ff))
print(g_sm)

