#!/usr/bin/env python3

with open('4.in', 'r') as f:
  G = f.readlines()

hits = 0
XMAS = "XMAS"
for y in range(len(G)):
  for x in range(len(G[y])):
    for d in [
      [(x+w, y+w) for w in range(len(XMAS))],
      [(x-w, y-w) for w in range(len(XMAS))],
      [(x-w, y+w) for w in range(len(XMAS))],
      [(x+w, y-w) for w in range(len(XMAS))],
      [(x+0, y+w) for w in range(len(XMAS))],
      [(x+w, y+0) for w in range(len(XMAS))],
      [(x+0, y-w) for w in range(len(XMAS))],
      [(x-w, y+0) for w in range(len(XMAS))],
    ]:
      for dx,dy in d:
        if dx < 0 or dy < 0 or dy >= len(G) or dx >= len(G[dy]):
          break
      else:
        hits += ''.join(G[dy][dx] for dx,dy in d) == XMAS
print(hits)

MS_SM = 'MS', 'SM'
hits = 0
for y in range(len(G)):
  for x in range(len(G[y])):
    if G[y][x] == 'A' and x >= 1 and x+1 < len(G[y]) and y >= 1 and y+1 < len(G):
      hits += G[y-1][x-1] + G[y+1][x+1] in MS_SM and G[y+1][x-1] + G[y-1][x+1] in MS_SM
print(hits)

