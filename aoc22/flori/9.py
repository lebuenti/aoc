#!/usr/bin/env python3

ll = [(x,int(n)) for x,n in [l.split(' ') for l in open('9.in').read().splitlines()]]
di = {'L': (1,0), 'R': (-1,0), 'U': (0,-1), 'D': (0,1)}

for knots in (1,9):
  Hx = Hy = 0
  T = [(Hx,Hy)] * knots
  Ts = {(Hx,Hy)}
  for mv,n in ll:
    for i in range(n):
      chx,chy = di[mv]
      Hx,Hy = (Hx+chx,Hy+chy)
      for k,(tx,ty) in enumerate(T):
        Px,Py = (Hx,Hy) if k == 0 else T[k-1]
        if (tx,ty) not in [
          (Px,Py),
          (Px+1,Py),
          (Px-1,Py),
          (Px,Py+1),
          (Px,Py-1),
          (Px+1,Py+1),
          (Px-1,Py-1),
          (Px+1,Py-1),
          (Px-1,Py+1),
        ]:
          if Py > ty:
            ty += 1
          elif Py < ty:
            ty -= 1
          if Px > tx:
            tx += 1
          elif Px < tx:
            tx -= 1
          T[k] = tx,ty
      Ts.add(T[-1])
  print(len(Ts))

