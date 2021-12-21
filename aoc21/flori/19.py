#!/usr/bin/env python

import numpy as np
from tqdm import tqdm


def permute():
  yield lambda a, b, c: (+a, +b, +c)
  yield lambda a, b, c: (+b, +c, +a)
  yield lambda a, b, c: (+c, +a, +b)
  yield lambda a, b, c: (+c, +b, -a)
  yield lambda a, b, c: (+b, +a, -c)
  yield lambda a, b, c: (+a, +c, -b)

  yield lambda a, b, c: (+a, -b, -c)
  yield lambda a, b, c: (+b, -c, -a)
  yield lambda a, b, c: (+c, -a, -b)
  yield lambda a, b, c: (+c, -b, +a)
  yield lambda a, b, c: (+b, -a, +c)
  yield lambda a, b, c: (+a, -c, +b)

  yield lambda a, b, c: (-a, +b, -c)
  yield lambda a, b, c: (-b, +c, -a)
  yield lambda a, b, c: (-c, +a, -b)
  yield lambda a, b, c: (-c, +b, +a)
  yield lambda a, b, c: (-b, +a, +c)
  yield lambda a, b, c: (-a, +c, +b)

  yield lambda a, b, c: (-a, -b, +c)
  yield lambda a, b, c: (-b, -c, +a)
  yield lambda a, b, c: (-c, -a, +b)
  yield lambda a, b, c: (-c, -b, -a)
  yield lambda a, b, c: (-b, -a, -c)
  yield lambda a, b, c: (-a, -c, -b)

inp = 'example.in'

with open(inp, 'r') as f:
  ll = f.read().splitlines()

scanners = []
for l in ll:
  if l.startswith('---'):
    scanners.append([])
  elif l == '':
    continue
  elif l[0].isdigit() or l[0] == '-':
    x,y,z = [int(n) for n in l.split(',')]
    scanners[-1].append(np.array([x,y,z]))


beacons = [*scanners[0]]

T = 1000  # max distance for a scanner to discover beacons

# sc * perms * beacs * sc * sc * beacs
for c, sc in enumerate(scanners[1:]):
  perm_mx_matches = 0
  perm_mn_unseen = []

  for perm in (progr := tqdm(permute(), total=24)):
    mx_matches, mn_unseen = 0, []
    progr.set_description(
      f"{c+1} of {len(scanners)-1} scanners, " \
      f"{len(beacons)} beacons")
    for ri in range(len(beacons)):
      for i in range(len(sc)):
        stck = np.stack([perm(*sc[i]), beacons[ri]])
        diff = np.diff(stck, axis=0).squeeze()

        sc_pos = np.zeros(3, int) + diff
        already, unseen, matches = [ri], [], 1
        range_beacs = []
        for beac in beacons:
          dists = np.absolute(np.diff(np.stack([beac, sc_pos]), axis=0))
          if np.all(dists <= T):
            range_beacs.append(beac)
          if len(range_beacs) >= 12:
            break
        for k in range(len(sc)):
          if k == i:
            continue
          upd = perm(*sc[k]) + diff
          matches_bef = matches
          for rk in range(len(range_beacs)):
            if rk in already:
              continue
            if np.all(upd == range_beacs[rk]):
              already.append(rk)
              matches += 1
          if matches_bef == matches:
            unseen.append(upd)

          if matches + (len(sc)-(k+1)) * (len(range_beacs)-(rk+1)) < mx_matches:
            break

        if matches > mx_matches:
          mx_matches = matches
          mn_unseen = unseen

    if mx_matches > perm_mx_matches:
      perm_mx_matches = mx_matches
      perm_mn_unseen = mn_unseen

  for un in perm_mn_unseen:
    exist = False
    for b in beacons:
      if np.all(un == b):
        exist = True
        break
    if not exist:
      beacons.append(un)

print(beacons)
print(len(beacons), 'beacons')

