def by_dir(d, n, coords):
  if d == 'N':
    coords[1]+=n
  elif d == 'S':
    coords[1]-=n
  elif d == 'W':
    coords[0]-=n
  elif d == 'E':
    coords[0]+=n
  else:
    raise Exception('no handler: ' + d)
  
def new_facing(facing, d, n):
  if d == 'R':
    return int((facing + n/90) % 4)
  elif d == 'L':
    return int((4 + ((facing - n/90) % 4)) % 4)
  else:
    raise Exception('no handler: ' + d)

nesw = ['N', 'E', 'S', 'W']
  
def do(ll):
  facing = 1
  coords= [0,0]
  for l in ll:
    d = l[0]
    n = int(l[1:])
    if d == 'R' or d == 'L':
      facing = new_facing(facing, d, n)
    elif d == 'F':
      by_dir(nesw[facing],n,coords)
    else:
      by_dir(d,n,coords)
  return do2(ll)

def do2(ll):
  # east by north
  wp =  [10, 1]
  ship = [0, 0]
  for l in ll:
    d = l[0]
    n = int(l[1:])
    if d == 'F':
      dist = [wp[0]-ship[0], wp[1]-ship[1]]
      ship[0] += dist[0]*n
      ship[1] += dist[1]*n
      wp[0] = ship[0] + dist[0]
      wp[1] = ship[1] + dist[1]
    elif d == 'R' or d == 'L':
      dist = (abs(abs(wp[0]) - abs(ship[0]))
            + abs(abs(wp[1]) - abs(ship[1])))
      circle = []
      for i in range(dist):
        circle.append([ship[0]-dist+i,ship[1]+i])  
      for i in range(dist):
        circle.append([ship[0]+i,ship[1]+dist-i])  
      for i in range(dist):
        circle.append([ship[0]+dist-i,ship[1]-i])  
      for i in range(dist):
        circle.append([ship[0]-i,ship[1]-dist+i])  
      if d == 'L':
        if n == 270:
          n = 90
        elif n == 90:
          n = 270
      ff = (circle.index(wp)+(((n/90))*dist))%len(circle)
      wp = circle[int(ff)]
    else:
      by_dir(d,n,wp)
  return abs(ship[0]) + abs(ship[1])

with open('12.in', 'r') as input:
  print("res", do(input.read().splitlines()))

