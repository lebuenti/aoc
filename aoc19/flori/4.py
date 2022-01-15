#!/usr/bin/env python3

A,B = 178416,676461

count = 0
for n in range(A+1, B):
  asstr = str(n)
  adjsame = False
  decrease = False
  for i in range(len(asstr)):
    if i != 0 and asstr[i-1] == asstr[i] and asstr.count(asstr[i]) == 2:
      adjsame = True
    if i != 0 and int(asstr[i]) < int(asstr[i-1]):
      decrease = True
      break
  if not adjsame or decrease:
    continue
  count += 1

print(count)

