#!/usr/bin/env python3

L = open('6.in').read().strip()
for n in (4,14):
  for i in range(n, len(L)):
    if len(set(L[i-n:i])) == n:
      print(i)
      break

