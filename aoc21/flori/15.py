#!/usr/bin/env python

from math import inf
from collections import defaultdict

with open('15.in', 'r') as f:
  grid1 = f.read().splitlines()

W = 9  # max weight

grid2 = []
for j in range(5):
  for y in range(len(grid1)):
    row = []
    for k in range(5):
      row.extend([(int(v)+j+k-1)%W+1 for v in grid1[y]])
    grid2.append(row)


class Vertex:
  def __init__(self, weight, x, y):
    self.w = int(weight)
    self.x, self.y = x, y

  def neigh(self, inp):
    res = []
    if self.y-1 > 0:
      res.append((self.y-1, self.x))
    if self.y+1 < len(inp):
      res.append((self.y+1, self.x))
    if self.x+1 < len(inp[self.y]):
      res.append((self.y, self.x+1))
    if self.x-1 >= 0:
      res.append((self.y, self.x-1))
    return [Vertex(inp[y][x], x, y) for y,x in res]

  def __repr__(self):
    return f"V(w={self.w}, x={self.x}, y={self.y})"

  def __hash__(self):
    return hash((self.x, self.y))

  def __eq__(self, o):
    if not isinstance(o, Vertex):
      return False
    return (o.x, o.y) == (self.x, self.y)
    

def Dial(grid, src):
  L = len(grid) * len(grid[0])

  dist = defaultdict(lambda: [inf, []])
  B = [[] for _ in range(W*L+1)]
  B[0].append(src)
  dist[src][0] = 0

  idx = 0
  while True:
    while len(B[idx]) == 0 and idx < W*L:
      idx += 1
    
    if idx == W * L:
      break

    u = B[idx].pop(0)
    
    for v in u.neigh(grid):
      du, dv = dist[u][0], dist[v][0]
      
      if dv > (du + v.w):
        if dv != inf:
          B[dv].remove(dist[v][1])

        dist[v][0] = du + v.w
        dv = dist[v][0]

        B[dv].insert(0, v)
        dist[v][1] = B[dv]

  return dist
    

src = Vertex(grid1[0][0], 0, 0)
for i, grid in enumerate([grid1, grid2]):
  y, x = len(grid)-1, len(grid[0])-1
  t = Vertex(grid[y][x], x, y)
  dist = Dial(grid, src)
  print(i+1, dist[t][0])

