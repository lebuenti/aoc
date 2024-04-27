#!/usr/bin/env python3

L = open('10.in').read(); START = "J"
ll = L.splitlines()

G = []
start = None
for y in range(len(ll)):
  g = []
  for x in range(len(ll[y])):
    if ll[y][x] == "S":
      start = x*2, y*2
      g.append(START)
    else:
      g.append(ll[y][x])
  G.append(g)
assert start is not None

# doubling resolution of G
J = {
  "F": ('-', '|'),
  "-": ('-', '.'),
  "|": ('.', '|'),
  "L": ('-', '.'),
  "J": ('.', '.'),
  "7": ('.', '|'),
  ".": ('.', '.'),
}
K = []
for y in range(len(G)):
  K.append([g for h in [(G[y][x], J[G[y][x]][0]) for x in range(len(G[y]))] for g in h])
  K.append([J[K[-1][x]][1] for x in range(len(K[-1]))])

loop = None
S = [([], start)]
while S:
  path, (x,y) = S.pop()
  if (x,y) in path:
    if (x,y) == start and len(path) > 2:
      if loop is None or len(path) < len(loop):
        loop = path
    continue
  nn = None
  if K[y][x] == "F":
    nn = [(x, y+1), (x+1, y)]
  elif K[y][x] == "-":
    nn = [(x-1, y), (x+1, y)]
  elif K[y][x] == "|":
    nn = [(x, y-1), (x, y+1)]
  elif K[y][x] == "L":
    nn = [(x, y-1), (x+1, y)]
  elif K[y][x] == "J":
    nn = [(x, y-1), (x-1, y)]
  elif K[y][x] == "7":
    nn = [(x, y+1), (x-1, y)]
  elif K[y][x] == ".":
    continue
  nn = [(xn,yn) for xn,yn in nn if xn >= 0 and yn >= 0 and xn < len(K[yn]) and yn < len(K)]
  assert nn is not None
  for n in nn:
    S.append(([*path, (x,y)], n))

assert len(loop) % 2 % 2 == 0
print(len(loop) // 2 // 2)


free = set()
alll = set()
S = [([], None, (x,y)) for y in range(len(K)) for x in range(len(K[y]))]
while S:
  tiles, isfree, (x,y) = S.pop()
  if (x,y) in alll:
    continue
  if (x,y) in tiles:
    continue
  if (x,y) in loop:
    continue
  alll.add((x,y))
  if isfree or (x == 0 or y == 0 or y == len(K)-1 or x == len(K[y])-1):
    isfree = True
    free |= set(tiles)
    free.add((x,y))
  for nx, ny in [
    (x-1,y+0),
    (x+1,y+0),
    (x+0,y-1),
    (x+0,y+1),
  ]:
    if nx < 0 or ny < 0 or ny >= len(K) or nx >= len(K[ny]):
      continue
    if isfree:
      ntiles = []
    else:
      ntiles = [*tiles, (x,y)]
    S.append((ntiles, isfree, (nx,ny)))

print(sum([(x,y) not in free and (x,y) in alll for y in range(0, len(K), 2) for x in range(0, len(K[y]), 2)]))

