#!/usr/bin/env python3

import re
from collections import Counter

PATTERN = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
L = open('3.in').read()
ll = L.splitlines()

K = {}
C = Counter()
for l in ll:
  ident,left,top,width,height =  \
    [int(n) for n in re.compile(PATTERN).match(l).groups()]
  K[ident] = set()
  for y in [y for y in range(top,top+height)]:
    for x in [x for x in range(left,left+width)]:
      C[x,y] += 1
      K[ident].add((x,y))

print(len([k for k,v in C.items() if v > 1]))

for ident,coords in K.items():
  for x,y in coords:
    if C[x,y] > 1:
      break
  else:
    print(ident)
    break

