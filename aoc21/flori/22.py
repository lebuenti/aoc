#!/usr/bin/env python

import itertools
from tqdm import tqdm


with open('22.in', 'r') as f:
  ll = f.read().splitlines()

D = []
for l in ll:
  sp1 = l.split(',')
  res = [None, None, None]
  nope = False
  for i,sp in enumerate(sp1):
    fi,ti = [int(x) for x in sp.split('=')[-1].split('..')]
    res[i] = (fi,ti)
    assert fi <= ti
  if not nope:
    D.append((l[:2] == 'on', res))


class Cuboid:
  def __init__(self, cubes):
    self.cubes = cubes
    self.inters = []

  def intersect(self, cubes):
    is_inters = True
    for dim in range(3):
      assert self.cubes[dim][0] <= self.cubes[dim][1]
      assert cubes[dim][0] <= cubes[dim][1]
      if not (self.cubes[dim][1] >= cubes[dim][0]
          and self.cubes[dim][0] <= cubes[dim][1]):
        is_inters = False
        break
    if not is_inters:
      return []
    res = [None, None, None]
    for dim in range(3):
      if cubes[dim][0] <= self.cubes[dim][0] \
          and cubes[dim][1] >= self.cubes[dim][1]:
        # entirely contained
        res[dim] = self.cubes[dim]
      elif cubes[dim][0] > self.cubes[dim][0] \
          and cubes[dim][1] < self.cubes[dim][1]:
        res[dim] = cubes[dim]
      elif cubes[dim][0] <= self.cubes[dim][0]:
        # overlaps left
        res[dim] = (self.cubes[dim][0],cubes[dim][1])
      elif self.cubes[dim][1] >= cubes[dim][0]:
        # overlaps right
        res[dim] = (cubes[dim][0],self.cubes[dim][1])

    for inter in self.inters:
      inter.intersect(res)

    self.inters.append(Cuboid(res))
    return self.inters[-1]

  def vol(self, res=True):
    on_vol = 1
    for dim in range(3):
      assert self.cubes[dim][1] >= self.cubes[dim][0]
      on_vol *= self.cubes[dim][1] - self.cubes[dim][0] + 1
    inter_vol = sum([inter.vol(res=False) for inter in self.inters])
    return on_vol - inter_vol


for i in range(2):

  ON = []
  for on, nx_cubes in D:
    if i == 0:
      if min(nx_cubes[0][0], nx_cubes[1][0], nx_cubes[2][0]) < -50:
        continue
      if max(nx_cubes[0][0], nx_cubes[1][1], nx_cubes[1][1]) > 50:
        continue

    for cuboid in ON:
      cuboid.intersect(nx_cubes)

    if on:
      ON.append(Cuboid(nx_cubes))

  print(sum([c.vol() for c in ON]))

