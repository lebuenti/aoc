#!/usr/bin/env python3

import re

L = open('1.in').read()
ll = L.splitlines()

dd = []
for l in ll:
  first, second = None, None
  for l1 in l:
    if l1.isdigit():
      if first is None:
        first = l1
      second = l1
  dd.append(int(first + second))
print(sum(dd))

N = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

firsts = []
for l in ll:
  idx_mn = None
  mn = None
  second = None
  for k,v in N.items():
    for n in (k, str(v)):
      if n not in l:
        continue
      idx = l.index(n)
      if idx_mn is None or idx_mn > idx:
        idx_mn = idx
        mn = v
  firsts.append(mn)

seconds = []
for l in ll:
  idx_mn = -1
  mn = None
  second = None
  for k,v in N.items():
    for n in (k, str(v)):
      if n not in l:
        continue
      idx = l.rindex(n)
      if idx_mn < idx:
        idx_mn = idx
        mn = v
  seconds.append(mn)

nums = [int(str(a) + str(b)) for a,b in zip(firsts, seconds)]
print(sum(nums))
