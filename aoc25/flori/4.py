#!/usr/bin/env python3

F = [[n for n in s] for s in open('4.in').read().splitlines()]
res = 0
while True:
  ch = set()
  for y in range(len(F)):
    for x in range(len(F[y])):
      if F[y][x] == '.':
        continue
      cnt = 0
      for nx, ny in [
        (x+0, y-1),
        (x+1, y-1),
        (x+1, y+0),
        (x+1, y+1),
        (x+0, y+1),
        (x-1, y+1),
        (x-1, y+0),
        (x-1, y-1),
      ]:
        if ny < 0 or ny >= len(F) or nx < 0 or nx >= len(F[ny]):
          continue
        cnt += F[ny][nx] == '@'
      if cnt < 4:
        ch.add((x,y))
  if len(ch) == 0:
    break
  for fx,fy in ch:
    F[fy][fx] = '.'
  if res == 0:
    print(len(ch))
  res += len(ch)
print(res)

