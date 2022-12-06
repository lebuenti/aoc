#!/usr/bin/env python3

from collections import deque
import heapq

IDENT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
L = open('20.in', 'r').read().splitlines()
#L = """
#         A           
#         A           
#  #######.#########  
#  #######.........#  
#  #######.#######.#  
#  #######.#######.#  
#  #######.#######.#  
#  #####  B    ###.#  
#BC...##  C    ###.#  
#  ##.##       ###.#  
#  ##...DE  F  ###.#  
#  #####    G  ###.#  
#  #########.#####.#  
#DE..#######...###.#  
#  #.#########.###.#  
#FG..#########.....#  
#  ###########.#####  
#             Z       
#             Z       
#""".splitlines()[1:]
#L = """
#                   A               
#                   A               
#  #################.#############  
#  #.#...#...................#.#.#  
#  #.#.#.###.###.###.#########.#.#  
#  #.#.#.......#...#.....#.#.#...#  
#  #.#########.###.#####.#.#.###.#  
#  #.............#.#.....#.......#  
#  ###.###########.###.#####.#.#.#  
#  #.....#        A   C    #.#.#.#  
#  #######        S   P    #####.#  
#  #.#...#                 #......VT
#  #.#.#.#                 #.#####  
#  #...#.#               YN....#.#  
#  #.###.#                 #####.#  
#DI....#.#                 #.....#  
#  #####.#                 #.###.#  
#ZZ......#               QG....#..AS
#  ###.###                 #######  
#JO..#.#.#                 #.....#  
#  #.#.#.#                 ###.#.#  
#  #...#..DI             BU....#..LF
#  #####.#                 #.#####  
#YN......#               VT..#....QG
#  #.###.#                 #.###.#  
#  #.#...#                 #.....#  
#  ###.###    J L     J    #.#.###  
#  #.....#    O F     P    #.#...#  
#  #.###.#####.#.#####.#####.###.#  
#  #...#.#.#...#.....#.....#.#...#  
#  #.#####.###.###.#.#.#########.#  
#  #...#.#.....#...#.#.#.#.....#.#  
#  #.###.#####.###.###.#.#.#######  
#  #.#.........#...#.............#  
#  #########.###.###.#############  
#           B   J   C               
#           U   P   P               
#""".splitlines()[1:]

K = {}
for y in range(len(L)):
  for x in range(len(L[y])):
    l = L[y][x]
    if not l.isalpha():
      continue
    for i,(nx,ny) in enumerate([(x+1,y),(x-1,y),(x,y+1),(x,y-1)]):
      try:
        n = L[ny][nx]
      except IndexError:
        continue
      if n != '.':
        continue
      o = L[y+(y-ny)][x+(x-nx)]
      if y < ny or x < nx:
        conn = o+l
      elif x > nx or y > ny:
        conn = l+o
      ident = IDENT[len(K)] 
      if conn == 'AA':
        start = ident
      elif conn == 'ZZ':
        target = ident
      K[ident] = (nx,ny), conn

assert start is not None
assert target is not None
print(f"from {start} to {target}")

Kpos = {pos: (ident,ft) for ident,(pos,ft) in K.items()}

G = []
for y in range(2,len(L)-2):
  G.append([])
  for x in range(2,len(L[y])-2):
    if (x,y) in Kpos:
      G[-1].append(Kpos[(x,y)][0])
    else:
      if L[y][x].isalpha():
        G[-1].append(' ')
      else:
        G[-1].append(L[y][x])

K = {ident: ((x-2,y-2),ft) for ident,((x,y),ft) in K.items()}
Kpos = {pos: (ident,ft) for ident,(pos,ft) in K.items()}

for g in G:
  print(''.join(g))

for k,v in sorted(K.items(), key=lambda x: x[1][1]):
  print(k,v)

def neighs(x,y):
  nn = []
  for c in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    try:
      g = G[c[1]][c[0]]
    except IndexError:
      continue
    if g != '#' and g != ' ':
      nn.append(c)
  return nn

M = {}
for ident,(pos,ft) in K.items():
  Q = deque([(frozenset(),pos)])
  while Q:
    seen,(x,y) = Q.popleft()
    if (x,y) in seen:
      continue
    seen = frozenset({*seen, (x,y)})
    if G[y][x] != start and G[y][x] != ident and G[y][x] in IDENT:
      if ident not in M:
        M[ident] = {}
      via = K[G[y][x]][1]
      cost = len(seen)
      if G[y][x] == target:
        M[ident][target] = cost-1
        print(f"from {ident} to H thru {G[y][x]} via {via} in {cost} steps")
      else:
        for ident1,(_,ft1) in K.items():
          if via == ft1 and G[y][x] != ident1:
            print(f"from {ident} to {ident1} thru {G[y][x]} via {via} in {cost} steps")
            M[ident][ident1] = cost
            break
      continue
    for n in neighs(x,y):
      Q.append((seen,n))

# dijkstra lazy expanding nodes
seen = set()
G = {start: 0}
P = {}
Q = [(0, start)]
while Q:
  g,n = heapq.heappop(Q)
  if n in seen:
    continue
  seen.add(n)
  if n == target:
    break
  for v,cost in M[n].items():
    vg = g + cost
    if v not in G or vg < G[v]:
      P[v] = n
      G[v] = vg
      heapq.heappush(Q, (vg, v))
print(G[target])

