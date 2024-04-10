#!/usr/bin/env python3

from math import lcm

L = open('8.in').read()
ll = L.splitlines()
dd = [int(l == "R") for l in ll[0]]

N = {}
for l in ll[2:]:
  spl = l.split(" = ")
  N[spl[0]] = tuple(spl[1][1:-1].split(", "))

n = "AAA"
step = 0
while n != "ZZZ":
  d = dd[step % len(dd)]
  n = N[n][d]
  step += 1
print(step)

nn = [n for n in N.keys() if n[-1] == "A"]
hit = [False] * len(nn)
step = 0
while not all(hit):
  for i, n in enumerate(nn):
    d = dd[step % len(dd)]
    nn[i] = N[n][d]
    if nn[i][-1] == "Z":
      if hit[i] is False:
        # went from start to end (this happens once)
        hit[i] = -(step + 1)
      elif hit[i] < 0:
        # went from end to end (this repeats infinitely)
        hit[i] += step
  step += 1
print(lcm(*hit))

