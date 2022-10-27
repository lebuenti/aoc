#!/usr/bin/env python3

with open('16.in', 'r') as f:
  nn = f.read()[:-1]
EXP, ITER = 1, 100
#nn = '12345678'; ITER = 1; EXP = 1
nn *= EXP
LEN = len(nn)

base = [0, 1, 0, -1]
contig = [0] * len(base)
for k in range(ITER):
  phase = ''
  for j in range(LEN):
    patti = 1 if j == 0 else 0
    sm = 0
    nni = 0
    while nni < LEN:
      end = nni+j+1
      if nni == 0:
        end = max(1, end-1)
      if patti == 1 or patti == 3:
        contig[patti] += sum([int(n) for n in nn[nni:end]])
      patti += 1
      if patti >= len(base):
        patti = 0
      nni = end
    sm = contig[1]*base[1] + contig[3]*base[3]
    contig[1] = 0
    contig[3] = 0
    one = str(sm)[-1]
    phase += one
  nn = phase
print('part1:', phase[:8])

