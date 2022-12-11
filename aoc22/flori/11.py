#!/usr/bin/env python3

from math import lcm

L1 = open('11.in').read()
L = [l.splitlines() for l in L1.split("\n\n")]

for part in (1,2):
  M = {}
  for l in L:
    ident = int(l[0][len("Monkey:")])
    M[ident] = {
      "wl": [int(n) for n in l[1].split(': ')[1].split(', ')],
      "op": eval(f"lambda old: {l[2].split(' = ')[1]}"),
      "test": int(l[3].split(' ')[-1]),
      "throw": (int(l[5].split(' ')[-1]), int(l[4].split(' ')[-1])),
    }
  if part == 2:
    mod = lcm(*[m["test"] for m in M.values()])

  insps = [0] * len(M)
  for i in range(20 if part == 1 else 10000):
    for k,m in M.items():
      for j,wl in enumerate(m["wl"]):
        insps[k] += 1
        new = m["op"](wl)
        if part == 1:
          new //= 3
        else:
          new %= mod
        div = int(new % m["test"] == 0)
        throw = m["throw"][div]
        M[throw]["wl"].append(new)
      m["wl"] = []

  insps.sort()
  print(insps[-1] * insps[-2])

