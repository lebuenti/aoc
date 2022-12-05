#!/usr/bin/env python3

stacks,moves = open('5.in').read().split("\n\n")

for part in (1,2):
  S = [0, *[[] for _ in range(int(stacks.strip()[-1]))]]
  for l in stacks.splitlines()[:-1]:
    idx = 1
    for i in range(1,len(l),4):
      if l[i] != ' ':
        S[idx].append(l[i])
      idx += 1

  for m in [l.split(' ') for l in moves.splitlines()]:
    num,fr,to = (int(m1) for m1 in m if m1.isdigit())
    mv = S[fr][:num]
    if part == 1:
      mv = mv[::-1]
    S[to] = [*mv, *S[to]]
    S[fr] = S[fr][num:]
  print(''.join([S[i][0] for i in range(1, len(S))]))

