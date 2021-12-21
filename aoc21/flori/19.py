#!/usr/bin/env python

from math import inf
import numpy as np
from tqdm import tqdm
from time import time


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
M = {
  '2dim.in': 3,
  '19.in': 12,
  'perm.in': -1,
  'example.in': -1,
}[inp]

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


def norm(beac):
  abso = np.absolute(beac)
  diff = np.diff([abso, np.zeros(len(abso), int)], axis=0).squeeze()
  mn = np.min(diff)
  norm = abso - mn
  return str(np.sum(norm))


beacons = [*scanners[0]]

def filt(beacons):
  s = time()
  SKIP = 1  # skip every SKIPth beacon in a sorted set
  stck = np.stack(beacons)
  res = []
  for dim in range(3):
    sort = stck[np.argsort(stck, axis=0)[:,dim]]
    last = False
    for i in range(0, len(sort), SKIP):
      res.append(sort[i])
      if i+1 == len(sort):
        last = True
    if not last:
      res.append(sort[-1])
  return res, time()-s


for c, sc in enumerate(scanners[1:]):
  perm_mx_matches = 0
  perm_mn_unseen = []
  filt_beacs, t = filt(beacons)
  print(f"{c+1} of {len(scanners)-1} scanners, " + \
        f"{len(beacons)} beacons, filt took {t:.4f}s")

  tt = []
  for perm in tqdm(permute(), total=24):
    mx_matches, mn_unseen = 0, []
    for ri in range(len(filt_beacs)):
      for i in range(len(sc)):
        stck = np.stack([perm(*sc[i]), filt_beacs[ri]])
        diff = np.diff(stck, axis=0).squeeze()

        already, unseen, matches = [ri], [], 1
        for k in range(len(sc)):
          if k == i:
            continue
          upd = perm(*sc[k]) + diff
          matches_bef = matches
          for rk in range(len(filt_beacs)):
            if rk in already:
              continue
            if np.all(upd == filt_beacs[rk]):
              already.append(rk)
              matches += 1
          if matches_bef == matches:
            unseen.append(upd)

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

