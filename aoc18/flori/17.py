#!/usr/bin/env python3

import re

water = set()
clay = set()
flow = set()

for l in open('17.in').read().splitlines():
  grps = re.compile("(.)=([0-9]+), (.)=([0-9]+)\.\.([0-9]+)").match(l).groups()
  rng = range(int(grps[3]), int(grps[4])+1)
  if grps[0] == 'x':
    clay |= {(int(grps[1]),y) for y in rng}
  else:
    assert grps[2] == 'x'
    clay |= {(x,int(grps[1])) for x in rng}

miny = min(y for _,y in clay)
maxy = max(y for _,y in clay)

water_sm = flow_sm = 0
sources = [(500, miny)]
while sources:
  sx,sy = sources.pop()
  bounds = clay | water

  # fall
  ny = sy
  while (sx,ny+1) not in (bounds | flow) and ny < maxy:
    ny += 1
    flow.add((sx,ny))
    assert (sx,ny) not in water

  if (sx,ny+1) in flow:
    continue

  if ny >= maxy:
    continue

  blocks = [None, None]
  falls = [None, None]
  for i,d in enumerate([-1, +1]):
    nx = sx+d
    while 1:
      if (nx,ny) in clay:
        blocks[i] = nx
        break
      if (nx,ny+1) not in bounds:
        falls[i] = nx
        break
      nx += d

  if falls[0] is not None or falls[1] is not None:
    if falls[0] is None and falls[1] is not None:
      # falls to the right
      fr,to = blocks[0]+1, falls[1]
      if (to,ny) not in sources:
        sources.insert(0, (to,ny))
    elif falls[1] is None and falls[0] is not None:
      # falls to the left
      fr,to = falls[0], blocks[1]-1
      if (fr,ny) not in sources:
        sources.insert(0, (fr,ny))
    elif falls[1] is not None and falls[0] is not None:
      # falls to both sides
      fr,to = falls[0], falls[1]
      if (fr,ny) not in sources:
        sources.insert(0, (fr,ny))
      if (to,ny) not in sources:
        sources.insert(0, (to,ny))
    else:
      raise Exception()

    for x1 in range(fr, to+1):
      flow.add((x1,ny))
      assert (x1,ny) not in water

    # clean the cache
    src_mn = min(y for _,y in sources)
    raw_sm = [0, 0]
    for i,c in enumerate([water, flow]):
      rms = []
      for q in c:
        if q[1] < src_mn:
          rms.append(q)
      for rm in rms:
        c.remove(rm)
      raw_sm[i] += len(rms)
    water_sm += raw_sm[0]
    flow_sm += raw_sm[1]
  else:
    # fill with water
    for x1 in range(blocks[0]+1, blocks[1]):
      water.add((x1,ny))
      if (x1,ny) in flow:
        flow.remove((x1,ny))

    # water level has risen to where water had previously flown
    f = None
    for d in (-1, +1):
      fn = sx,ny-1
      while fn in flow:
        flow.remove(fn)
        if fn in sources:
          sources.remove(fn)
        if (fn[0],fn[1]-1) in flow:
          f = (fn[0],fn[1]-1)
        fn = fn[0]+d, fn[1]

    if f is None:
      f = sx,ny-1
    if f not in sources:
      sources.append(f)

print(len(flow) + len(water) + water_sm + flow_sm)
print(len(water) + water_sm)

