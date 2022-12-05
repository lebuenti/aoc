#!/usr/bin/env python3

ll = open('5.in').read().split("\n\n")
mm = [l.split(' ') for l in ll[1].splitlines()]

for i in range(len(mm)):
  mm[i] = tuple([int(m) for m in mm[i] if m.isdigit()])

for part in (1,2):
  S = [0, *[[] for _ in range(int(ll[0].strip()[-1]))]]
  for l in ll[0].splitlines()[:-1]:
    idx = 1
    for i in range(1,len(l),4):
      if l[i] != ' ':
        S[idx].append(l[i])
      idx += 1

  for num,fr,to in mm:
    if part == 1:
      S[to] = [*S[fr][:num][::-1], *S[to]]
    else:
      S[to] = [*S[fr][:num], *S[to]]
    S[fr] = S[fr][num:]
  print(''.join([S[i][0] for i in range(1, len(S))]))

