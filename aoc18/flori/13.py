#!/usr/bin/env python3

R = open('13.in').read()[:-1].splitlines()

#     0    1    2    3
F = ('<', '>', 'v', '^')
D = ((-1,0), (+1,0), (0,+1), (0,-1))
LEFT, STRAIGHT, RIGHT = 0, 1, 2
C = []
for y in range(len(R)):
  for x in range(len(R[y])):
    if R[y][x] in F:
      C.append(((x,y), F.index(R[y][x]), LEFT))
      R[y] = R[y][:x] + ('|' if R[y][x] in ('v','^') else '-') + R[y][x+1:]

part1 = True
while len(C) > 1:
  C.sort()
  crashed = set()
  for i,((x,y),f,t) in enumerate(C):
    if i in crashed:
      continue
    nx,ny = x+D[f][0], y+D[f][1]
    if (nx,ny) in [pos for pos,*_ in C]:
      if part1:
        print(f"{nx},{ny}")
        part1 = False
      crashed.add(i)
      for k,(pos1,*_) in enumerate(C):
        if i != k and pos1 == (nx,ny):
          crashed.add(k)
          break
      else:
        raise Exception()
    nr = R[ny][nx]
    nf = f
    nt = t
    if nr == '\\':
      if f == 0:
        nf = 3
      elif f == 1:
        nf = 2
      elif f == 2:
        nf = 1
      elif f == 3:
        nf = 0
    elif nr == '/':
      if f == 0:
        nf = 2
      elif f == 1:
        nf = 3
      elif f == 2:
        nf = 0
      elif f == 3:
        nf = 1
    elif nr == '+':
      if t != STRAIGHT:
        assert t == LEFT or t == RIGHT
        # right is three times left
        for turns in range(1 if t == LEFT else 3):
          if nf == 0:
            nf = 2
          elif nf == 1:
            nf = 3
          elif nf == 2:
            nf = 1
          elif nf == 3:
            nf = 0
      nt = (t+1) % 3
    elif nr == '|':
      assert f == 2 or f == 3
    elif nr == '-':
      assert f == 0 or f == 1
    else:
      raise Exception(nr)
    C[i] = (nx,ny), nf, nt
  for i in sorted(crashed)[::-1]:
    C.pop(i)
  crashed.clear()
print(f"{C[0][0][0]},{C[0][0][1]}")

