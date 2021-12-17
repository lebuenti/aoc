#!/usr/bin/env python


with open('17.in', 'r') as f:
  ll = f.read().strip()
  a,b,c = ll.split('..')
  tx = (int(a.split('=')[-1]), int(b.split(',')[0]))
  ty = (int(b.split('=')[-1]), int(c.split(',')[-1]))


max_py = 0
inits = set()

for init_vy in range(ty[0]-1, abs(ty[0]-ty[1])*3):  # 3 is arbitrary
  px, py = 0, 0
  vx, vy = 0, init_vy

  for init_vx in range(1, tx[1]+1):
    vx = init_vx
    vy = init_vy
    px, py = 0, 0

    curr_max_py = 0
    while True:  # step
      px = px+vx
      py = py+vy
      vx = vx+1 if vx < 0 else vx-1 if vx != 0 else vx
      vy = vy-1

      curr_max_py = max(curr_max_py, py)

      if px >= tx[0] and px <= tx[1] \
          and py >= ty[0] and py <= ty[1]:
        # strike
        strike = True
        break

      if px > tx[1] or py < ty[0]:
        # undershot or overshot
        strike = False
        break

    if strike:
      inits.add((init_vx, init_vy))
      max_py = curr_max_py


print('1', max_py)
print('2', len(inits))

