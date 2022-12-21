#!/usr/bin/env python3

L = open('20.in').read().splitlines()
for it,key in ((1, 1), (10, 811589153)):
  MASK = {n: int(v) * key for n,v in enumerate(L)}
  op = list(MASK.keys())

  for _ in range(it):
    for n,v in MASK.items():
      idx = op.index(n)
      op.insert((idx + v) % (len(op) - 1), op.pop(idx))

  unmasked = [MASK[n] for n in op]
  zero = unmasked.index(0)
  print(sum(unmasked[(zero + i) % len(unmasked)] for i in (1000, 2000, 3000)))

