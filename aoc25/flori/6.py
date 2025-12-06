#!/usr/bin/env python3

from math import prod

F = open('6.in').read().splitlines()
OP = {'*': prod, '+': sum}
P = [(i,F[-1][i]) for i in range(len(F[-1])) if F[-1][i] != ' ']
p1 = p2 = 0
for j in range(len(P)):
  end = P[j+1][0]-1 if j < len(P)-1 else len(F[0])
  nn = [F[y][P[j][0]:end] for y in range(len(F)-1)]
  op = OP[P[j][1]]
  p1 += op(int(n) for n in nn)
  ln = max(len(n) for n in nn)
  p2 += op(int(''.join(n[i] for n in nn)) for i in range(ln-1, -1, -1))
print(p1)
print(p2)

