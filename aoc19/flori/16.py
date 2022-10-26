#!/usr/bin/env python3

with open('16.in', 'r') as f:
  nn = f.read()[:-1]

base = [0, 1, 0, -1]
for k in range(100):
  phase = ''
  for j in range(len(nn)):
    patti = 1 if j == 0 else 0
    reps = 1
    sm = 0
    for i in range(len(nn)):
      if reps > 0 and reps % (j+1) == 0:
        patti += 1
        if patti >= len(base):
          patti = 0
          reps = 0
      fac = base[patti]
      reps += 1
      sm += int(nn[i]) * fac
    one = str(sm)[-1]
    phase += one
  nn = phase
print('part1:', phase[:8])

