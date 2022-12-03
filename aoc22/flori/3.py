#!/usr/bin/env python3

ABC = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ll = open('3.in').read().splitlines()

sm1, sm2 = 0, 0
for i in range(0, len(ll), 3):
  for l in ll[i:i+3]:
    c1,c2 = l[:len(l)//2],l[len(l)//2:]
    assert len(c1) == len(c2)
    sm1 += sum(set([ABC.index(c1c) for c1c in c1 if c1c in c2]))
  mm = set([c1c for c1c in ll[i] if c1c in ll[i+1]])
  sm2 += sum(set([ABC.index(c1c) for c1c in ll[i+2] if c1c in mm]))
print(sm1)
print(sm2)

