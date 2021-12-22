#!/usr/bin/env python

from tqdm import trange
from collections import defaultdict

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

def create_diff(a, b):
  return a[0]-b[0], a[1]-b[1], a[2]-b[2]

def apply_diff(a, b):
  return a[0]+b[0], a[1]+b[1], a[2]+b[2]

with open('19.in', 'r') as f:
  ll = f.read().splitlines()

sc = []
for l in ll:
  if l.startswith('---'):
    sc.append([])
  elif l == '':
    continue
  elif l[0].isdigit() or l[0] == '-':
    x,y,z = [int(n) for n in l.split(',')]
    sc[-1].append((x,y,z))

# ground-truth beacons
gt_sc = [None] * len(sc)
gt_sc[0] = [*sc[0]]

# ground-truth scanner positions
gt_sc_pos = [None] * len(sc)
gt_sc_pos[0] = (0,0,0)

DP = defaultdict(lambda: True)
while gt_sc.count(None):
  bef = gt_sc.count(None)
  for i in (progr := trange(len(sc))):
    if gt_sc[i] is not None:
      continue  # scanner already ground-truthed

    # match unknown sc against ground-truthed sc
    for gt_i in range(len(gt_sc)):
      if gt_sc[gt_i] is None:
        continue
      if gt_i == i:
        continue
      if not DP[gt_i, i]:
        continue

      mx_perm, mx_perm_match_count, mx_perm_diff = None, -1, None
      for perm in permute():
        mx_diff, mx_match_count = None, -1
        for bi in range(len(sc[i])):
          for gt_bi in range(len(gt_sc[gt_i])):
            diff = create_diff(gt_sc[gt_i][gt_bi], perm(*sc[i][bi]))
            match_count = 1
            for bj in range(len(sc[i])):
              upd = apply_diff(perm(*sc[i][bj]), diff)
              for gt_bj in range(len(gt_sc[gt_i])):
                if gt_bj == gt_bi:
                  continue
                if upd == gt_sc[gt_i][gt_bj]:
                  match_count += 1
            if match_count > mx_match_count:
              mx_match_count = match_count
              mx_diff = diff
        if mx_match_count > mx_perm_match_count:
          mx_perm = perm
          mx_perm_match_count = mx_match_count
          mx_perm_diff = mx_diff

      if mx_perm_match_count >= 12:
        gt_sc[i] = [apply_diff(mx_perm(*beac),mx_perm_diff) for beac in sc[i]]
        gt_sc_pos[i] = mx_perm_diff
        progr.set_description(str(gt_sc.count(None)) + " left")
        break
      DP[gt_i, i] = False

    if bef != gt_sc.count(None):
      break  # seems faster than continue

print(len(set([y for x in gt_sc for y in x])))

mx = -1
for i in range(len(gt_sc_pos)):
  for k in range(len(gt_sc_pos)):
    if i == k:
      continue
    n = abs(gt_sc_pos[i][0]-gt_sc_pos[k][0]) \
      + abs(gt_sc_pos[i][1]-gt_sc_pos[k][1]) \
      + abs(gt_sc_pos[i][2]-gt_sc_pos[k][2])
    mx = max(mx, n)

print(mx)

