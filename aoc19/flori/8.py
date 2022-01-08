#!/usr/bin/env python3

with open('8.in', 'r') as f:
  r = f.read().strip()

WIDE, TALL = 25, 6
r = list(map(int, r))

L = []
while r:
  l = []
  for t in range(TALL):
    row = []
    for w in range(WIDE):
      row.append(r.pop(0))
    l.append(row)
  L.append(l)

few, few_l = None, None
for l in L:
  f = [k for j in l for k in j]
  c = f.count(0)
  if few is None or c < few:
    few = c
    few_l = f
  
print(few_l.count(1) * few_l.count(2))

for t in range(TALL):
  for w in range(WIDE):
    v = [l[t][w] for l in L if l[t][w] != 2][0]
    print('x' if v == 1 else ' ', end='')
  print()
        
