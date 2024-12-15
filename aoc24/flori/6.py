#!/usr/bin/env python3

with open('6.in', 'r') as f:
  G = f.readlines()

GUARD, DOT, HASH = "^", ".", "#"
UP, DOWN, LEFT, RIGHT = "UP", "DOWN", "LEFT", "RIGHT"
MOVE = [UP, RIGHT, DOWN, LEFT]

for y in range(len(G)):
  if GUARD in G[y]:
    start = G[y].index(GUARD), y
    break

def step(gx, gy, d, extra_obstruction=None):
  if gx == 0 or gy == 0 or gx == len(G[gy])-1 or gy == len(G)-1:
    return False
  if d == UP:
    n = gx, gy-1
  elif d == RIGHT:
    n = gx+1, gy
  elif d == DOWN:
    n = gx, gy+1
  elif d == LEFT:
    n = gx-1, gy
  if G[n[1]][n[0]] == HASH or n == extra_obstruction:
    return gx, gy, MOVE[(MOVE.index(d)+1) % len(MOVE)]
  return *n, d

s = *start, UP
steps = {start}
while s := step(*s):
  steps.add(s[:2])
print(len(steps))

hit = 0
for obstr in steps - {start}:
  seen = set()
  s = *start, UP
  while s := step(*s, obstr):
    if s in seen:
      hit += 1
      break
    seen.add(s)
print(hit)

