#!/usr/bin/env python3

L = open('18.in').read()
ll = [tuple(int(n) for n in l.split(',')) for l in L.splitlines()]

def sides(x,y,z):
  return {
    (x+1, y,   z),
    (x-1, y,   z),
    (x,   y+1, z),
    (x,   y-1, z),
    (x,   y,   z+1),
    (x,   y,   z-1),
  }

def area(coords):
  surface = 0
  for x,y,z in coords:
    surf = 6
    for nx,ny,nz in sides(x,y,z):
      if (nx,ny,nz) in coords:
        surf -= 1
    surface += surf
  return surface
print(surface := area(ll))

xx = {x for x,_,_ in ll}
yy = {y for _,y,_ in ll}
zz = {z for _,_,z in ll}
minx, miny, minz = min(xx), min(yy), min(zz)
maxx, maxy, maxz = max(xx), max(yy), max(zz)

pocketed = set()
for x in range(minx+1, maxx):
  for y in range(miny+1, maxy):
    for z in range(minz+1, maxz):
      if (x,y,z) in ll:
        continue
      if (x,y,z) in pocketed:
        continue
      seen = set()
      S = [(x,y,z)]
      while S:
        V = S.pop()
        x1,y1,z1 = V
        if V in seen:
          continue
        seen.add(V)
        if x1 >= maxx or x1 <= minx \
        or y1 >= maxy or y1 <= miny \
        or z1 >= maxz or z1 <= minz:
          # reached outer shell, xyz is not air pocketeted
          break
        for n in sides(x1,y1,z1):
          if n not in ll:
            S.append(n)
      else:
        # all in seen is air pocketed
        pocketed.update(seen)

print(surface - area(pocketed))

