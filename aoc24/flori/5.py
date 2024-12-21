#!/usr/bin/env python3

with open('5.in', 'r') as f:
  L = f.read().splitlines()

O = [[int(n) for n in l.split(",")] for l in L if "," in l]
K = {}
for l in L:
 if l == "":
  break
 b,a = l.split("|")
 if int(b) not in K:
  K[int(b)] = []
 K[int(b)].append(int(a))

ww = []
sm = 0
for oo in O:
  res = True
  for i in range(len(oo)):
    oob = oo[:i]
    o = oo[i]
    ooa = oo[i+1:]
    for oa in ooa:
      if oa not in K:
        continue
      if o in K[oa]:
        res = False
        break
    if res is False:
      break
  if res:
    sm += oo[len(oo) // 2]
  else:
    ww.append(oo)
print(sm)

sm = 0
for oo in ww:
  i = 0
  while i < len(oo):
    o = oo[i]
    ooa = oo[i+1:]
    res = True
    for k,oa in enumerate(ooa):
      if oa not in K:
        continue
      if o in K[oa]:
        res = False
        break
    if res is False:
      oo[i+k], oo[i+k+1] = oo[i+k+1], oo[i+k]
      i = 0
      continue
    i+=1
  sm += oo[len(oo) // 2]
print(sm)

