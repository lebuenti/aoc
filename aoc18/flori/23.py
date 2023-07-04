#!/usr/bin/env python3

import heapq

ll = open('23.in').read().splitlines()
DIM = 0, 1, 2
N = []
for l in ll:
  sp = l.split(', ')
  N.append((int(sp[1][2:]), [int(n) for n in sp[0][len('pos=<'):-1].split(',')]))
N.sort()

r, (sx,sy,sz) = N[-1]
print(sum([(abs(x-sx) + abs(y-sy) + abs(z-sz)) <= r for _, (x,y,z) in N]))

xyz = [[xyz[i] for _,xyz in N] for i in DIM]
(mn_x, mx_x), (mn_y, mx_y), (mn_z, mx_z) = \
  [(min(xyz[i]), max(xyz[i])) for i in DIM]
B_init = (mn_x, mn_y, mn_z), (mx_x, mx_y, mx_z)
B_size = \
    (abs(mn_x) + abs(mx_x+abs(mn_x))) \
  * (abs(mn_y) + abs(mx_y+abs(mn_y))) \
  * (abs(mn_z) + abs(mx_z+abs(mn_z)))


def intersect(b, n):
  r, xyz = n
  d = 0
  for i in DIM:
    b_lo, b_hi = b[0][i], b[1][i] - 1
    d += abs(xyz[i] - b_lo) + abs(xyz[i] - b_hi)
    d -= b_hi - b_lo
  return d // 2 <= r


Q = [(-len(N), -B_size, B_size, B_init)]
while Q:
  (sm, size, dist, b) = heapq.heappop(Q)
  if size == -1:
    print(dist)
    break
  b_size = size // -2
  for ch in [
    (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
    (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
  ]:
    b_new = \
      (b0 := tuple(b[0][i] + b_size * ch[i] for i in DIM)), \
      tuple(b0[i] + b_size for i in DIM)
    sm_new = sum(intersect(b_new, n) for n in N)
    heapq.heappush(Q, (-sm_new, -b_size, sum(b0), b_new))

