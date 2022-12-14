#!/usr/bin/env python3

from collections import deque
from functools import cmp_to_key as cmp

ll = [eval(x) for y in [l.splitlines() for l in open('13.in').read().split("\n\n")] for x in y]

def zipfill(v1,v2):
  # itertools.zip_longest(v1,v2,fillvalue=None)
  return list(zip(*[[None if z >= len(v) else v[z] for z in range(0, max(len(v1),len(v2)))] for v in (v1,v2)]))

def srt(a,b):
  S = deque(zipfill(a,b))
  while S:
    v1,v2 = S.popleft()
    assert not (v1 is None and v2 is None)
    if isinstance(v1, int) and isinstance(v2, int):
      if v1 < v2:
        return 1
      elif v1 > v2:
        return -1
    elif isinstance(v1, list) and isinstance(v2, list):
      S.extendleft(zipfill(v1,v2)[::-1])
    elif v1 is None:
      return 1
    elif v2 is None:
      return -1
    else:
      fll = ([v1],v2) if isinstance(v1, int) else (v1,[v2])
      S.extendleft(zipfill(*fll)[::-1])

print(sum(min(1, srt(*ll[i:i+2]) + 1) * ((i + 2) // 2) for i in range(0, len(ll), 2)))

ll.extend(divs := ([[2]], [[6]]))
thesort = sorted(ll, reverse=True, key=cmp(srt))
print((thesort.index(divs[0])+1)*(thesort.index(divs[1])+1))

