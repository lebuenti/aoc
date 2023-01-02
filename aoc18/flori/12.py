#!/usr/bin/env python3

L = open('12.in').read().split("\n\n")
K = {i: s == '#' for i,s in enumerate([c for c in L[0].split(': ')[1]])}
notes = []
for note in L[1].splitlines():
  nn,n = note.split(' => ')
  notes.append(([c == '#' for c in nn], n == '#'))

N = 50000000000
diff = prev = here = -1
for g in range(N):
  here = sum(k for k in sorted(K) if K[k])
  if diff == (diff := here - prev):
    print((N - g) * diff + here)
    break
  prev = here
  if g == 20:
    print(prev)
  mink = min(K.keys())
  K[mink-1] = False
  K[mink-2] = False
  K[mink-3] = False
  maxk = max(K.keys())
  K[maxk+1] = False
  K[maxk+2] = False
  K[maxk+3] = False
  Kn = {}
  for pos,plant in K.items():
    for v,p in notes:
      if [False if i not in K else K[i] for i in range(pos-2, pos+3)] == v:
        Kn[pos] = p
        break
    else:
      Kn[pos] = False
  K = Kn

