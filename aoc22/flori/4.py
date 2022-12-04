#!/usr/bin/env python3

sm1, sm2 = 0, 0
for l in [l.split(',') for l in open('4.in').read().splitlines()]:
  rr = []
  for li in l:
    r = li.split('-')
    rr.append(range(int(r[0]), int(r[1])+1))
  it, ot = sorted(rr, key=lambda x: len(x))
  sm1 += set(it).issubset(ot)
  for i in range(len(it)):
    if it[i] in ot:
      sm2 += 1
      break
print(sm1)
print(sm2)

