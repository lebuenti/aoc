#!/usr/bin/env python

with open('25.in', 'r') as f:
  inp = f.read()

ll = inp
ll = [[c for c in x] for x in ll.splitlines()]
[print(''.join(l)) for l in ll]
print()

curr = ll
step = 1
while 1:
  upd = [[*l] for l in curr]
  bef = str(upd)
  for y in range(len(curr)):
    for x in range(len(curr[y])):
      fig = curr[y][x]
      if fig == '>':
        if x+1 == len(curr[y]):
          if curr[y][0] == '.':
            upd[y][0] = '>'
            upd[y][x] = '.'
        elif curr[y][x+1] == '.':
          upd[y][x+1] = '>'
          upd[y][x] = '.'

  curr = upd
  upd = [[*l] for l in curr]
  for y in range(len(curr)):
    for x in range(len(curr[y])):
      fig = curr[y][x]
      if fig == 'v':
        if y+1 == len(curr):
          if curr[0][x] == '.':
            upd[0][x] = 'v'
            upd[y][x] = '.'
        elif curr[y+1][x] == '.':
          upd[y+1][x] = 'v'
          upd[y][x] = '.'

  curr = upd

  print()
  print('step', step)
  [print(''.join(l)) for l in upd]

  if bef == str(curr):
    break

  step += 1

