#!/usr/bin/env python3

from collections import deque
from math import inf

def iskey(g):
  return g.isalpha() and g.islower()

def isdoor(g):
  return g.isalpha() and g.isupper()

def iswalkable(g, coll):
  return g.lower() in coll or iskey(g) or g == '.' or g == '@'

def nice(x,y,coll):
  print()
  print((x,y), coll)
  for gy in range(len(G)):
    for gx in range(len(G[y])):
      p = None
      g = G[gy][gx]
      if x == gx and y == gy:
        p = '@'
      elif g.lower() in coll or g == '@':
        p = '.'
      print(p or g, end='')
    print()

L = open('18.in', 'r').read()
#L = """
##########
##b.A.@.a#
##########
#"""
#L = """
#########################
##f.D.E.e.C.b.A.@.a.B.c.#
#######################.#
##d.....................#
#########################
#"""
G = L.strip().splitlines()
root = None
keys = set()
for y in range(len(G)):
  for x in range(len(G[y])):
    if G[y][x] == '@':
      root = x,y
    if iskey(G[y][x]):
      keys.add(G[y][x])
    print(G[y][x], end='')
  print()

print(root)
print(keys)

def neighs(x,y,coll):
  cands = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
  ret = []
  for x1,y1 in cands:
    if x1 >= 0 and x1 < len(G[y]) \
    and y1 >= 0 and y1 < len(G) \
    and iswalkable(G[y1][x1], coll):
      ret.append((x1,y1))
  return ret

pp = []
Q = deque([(set(),[],root)])
mn = inf
while len(Q) > 0:
  coll,path,(x,y) = Q.pop()
  g = G[y][x]
  if colled := iskey(g) and g not in coll:
    coll = {*coll, g}
  prev = None if len(path) == 0 else path[-1]
  path = [*path, (x,y)]
  if len(path) >= mn:
    continue
  if coll == keys:
    pp.append(path)
    print(len(path)-1)
    mn = min(len(path)-1, mn)
    continue
  for n in neighs(x,y,coll):
    if colled or n != prev:
      Q.append((coll,path,n))

for p in pp:
  print(len(p)-1, p)
print('part1:', min([len(p)-1 for p in pp]))

