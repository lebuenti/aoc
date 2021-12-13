#!/usr/bin/env python

with open('13.in', 'r') as f:
  reada, readb = f.read().split('\n\n')

dots = []
for ra in reada.splitlines():
    dots.append(tuple(map(int, ra.split(','))))

folds = []
for rb in readb.splitlines():
  one, two = rb.split('=')
  c, num = one[-1], int(two)
  folds.append((c, int(num)))
  
w, h = max([d[0] for d in dots])+1, max([d[1] for d in dots])+1
G = [['.'] * w for i in range(h)]
for x,y in dots:
  G[y][x] = '#'

for ax,n in folds:
  if ax == 'y':
    g1, g2 = G[:n], G[n+1:][::-1]
    h //= 2
  elif ax == 'x':
    g1, g2 = [], []
    for y in range(h):
      g1.append(G[y][:n])
      g2.append(G[y][n+1:][::-1])
    w //= 2

  new = []
  for y in range(len(g1)):
    new.append(['.'] * len(g1[y]))
    for x in range(len(g1[y])):
      new[y][x] = '#' if '#' in g1[y][x]+g2[y][x] else '.'
  G = new

  print(ax,n)
  for y in G:
    for x in y:
      print(x, end='')
    print()
  print()


print(len([x for g in G for x in g if x == '#']))

