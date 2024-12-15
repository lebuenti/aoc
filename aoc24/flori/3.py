#!/usr/bin/env python3

with open('3.in', 'r') as f:
  X = ''.join(f.readlines())

for part in (1,2):
  act = False
  do = True
  i = sm = 0
  while i < len(X):
    if act:
      buff = ""
      k = 0
      while X[i+k].isdigit():
        buff += X[i+k]
        k += 1
      if X[i+k] == ',':
        prod = max(int(buff), prod * int(buff))
        i += k
      elif X[i+k] == ')':
        sm += prod * int(buff)
        i += k
        act = False
      else:
        act = False
        prod = 0
    else:
      if X[i:i+7] == "don't()":
        do = False
      elif X[i:i+4] == "do()":
        do = True
      elif X[i:i+4] == "mul(" and (do or part == 1):
        act = True
        i += 3
        prod = 0
    i += 1
  print(sm)

