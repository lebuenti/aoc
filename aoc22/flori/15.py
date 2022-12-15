#!/usr/bin/env python3

from collections import deque
import re

def unoverlap(ranges):
  ret = []
  Q = deque(sorted({*ranges}))
  while Q:
    cs,ce = Q.popleft()
    end = None
    for j,(js,je) in enumerate(Q):
      js,je = Q[j]
      if js < ce:
        ce = max(je,ce)
      else:
        ret.append((cs,ce))
        end = j
        break
    if end is None:
      ret.append((cs,ce))
      return ret
    else:
      for _ in range(end):
        Q.popleft()
  return ret

Y = 2000000
K = 4_000_000
ll = open('15.in').read().splitlines()

PATTERN = "Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)"
sensors = []
beacons = []
for l in ll:
  sx,sy,bx,by = [int(n) for n in re.compile(PATTERN).match(l).groups()]
  sensors.append((sx,sy))
  beacons.append((bx,by))

for y in range(K+1):
  part1 = set()
  ranges = []
  for i,s in enumerate(sensors):
    bx,by = beacons[i]
    sx,sy = s
    w = abs(sx-bx)+abs(by-sy)
    fy,ty = sy-w, sy+w
    if y != Y and (ty < 0 or fy > K):
      continue
    assert fy < ty
    if y >= fy and y <= ty:
      d = abs(y-sy)
      fx, tx = sx-w+d, sx+w-d
      if y == Y:
        part1.add((fx,tx))
      if tx < 0 or fx > K:
        continue
      fx, tx = max(fx,0),min(tx+1,K)
      ranges.append((fx,tx))

  if y == Y:
    print(len({x for y in [range(s,e+1) for s,e in part1] for x in y}) - len({y for _,y in beacons if y == Y}))

  ranges = unoverlap(ranges)
  for j in range(len(ranges)-1):
    if ranges[j][1] - ranges[j+1][0] == -1:
      print(ranges[j][1] * 4000000 + y)
      exit()

