#!/usr/bin/env python

import re

  
def nice(G):
  for y in G:
    for x in y:
      print(x, end='')
    print()
  print()


def merge(g1, g2):
  new = []
  for y in range(len(g1)):
    new.append(['.'] * len(g1[y]))
    for x in range(len(g1[y])):
      if g1[y][x] == '#' or g2[y][x] == '#':
        new[y][x] = '#'
  return new


with open('13.in', 'r') as f:
  ll = f.read().splitlines()

dots, folds = [], []
doingfordots = True
for l in ll:
  if l == '':
    doingfordots = False
  elif doingfordots:
    dots.append(tuple([int(i) for i in l.split(',')]))
  else:
    c, num = re.findall("^fold along ([xy])=([0-9]+)$", l)[0]
    folds.append((c, int(num)))
  
w, h = max([d[0] for d in dots])+1, max([d[1] for d in dots])+1
G = [['.'] * w for i in range(h)]
for x,y in dots:
  G[y][x] = '#'

for ax,n in folds:
  if ax == 'y':
    if '#' in G[n]:
      raise Exception()
    G = merge(G[:n], G[n+1:][::-1])
    h //= 2
  elif ax == 'x':
    g1, g2 = [], []
    for y in range(h):
      g1.append(G[y][:n])
      g2.append(G[y][n+1:][::-1])
    G = merge(g1, g2)
    w //= 2
  print(ax,n)
  nice(G)
    
print(len([x for g in G for x in g if x == '#']))

  



  
