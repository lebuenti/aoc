def dictify(ll):
  d = {}
  for y in range(len(ll)):
    d[y] = {}
    for x in range(len(ll[y])):
      d[y][x] = ll[y][x]
  return d

def neighbors(xyzw):
  nn = []
  curr = []
  for x_diff in [-1,0,1]:
    curr = [xyzw[0]+x_diff]
    for y_diff in [-1,0,1]:
      curr.append(xyzw[1]+y_diff)
      for z_diff in [-1,0,1]:
        curr.append(xyzw[2]+z_diff)
        for w_diff in [-1,0,1]:
          curr.append(xyzw[3]+w_diff)
          nn.append([*curr])
          curr.pop(3)
        curr.pop(2)
      curr.pop(1)
    curr.pop(0)
  nn.pop(nn.index(xyzw))
  return nn

def next_state(cube, act):
  if cube == '#':
    if act in [2,3]:
      return '#'
    else:
      return '.'
  elif cube == '.':
    if act == 3:
      return '#'
    else:
      return '.'
  raise Exception("cube is neither . nor #: " + cube)

def expand(D):
  DC={}
  for w in list(D.keys()):
    DC[w]={}
    for z in list(D[w].keys()):
      DC[w][z]={}
      for y in list(D[w][z].keys()):
        DC[w][z][y]={}
        for x,cube in list(D[w][z][y].items()):
          nn = neighbors([x,y,z,w])
          for n in nn:
            try:
              DC[n[3]][n[2]][n[1]][n[0]]=D[n[3]][n[2]][n[1]][n[0]]
            except KeyError:
              if n[3] not in DC:
                DC[n[3]] = {}
              if n[2] not in DC[n[3]]:
                DC[n[3]][n[2]] = {}
              if n[1] not in DC[n[3]][n[2]]:
                DC[n[3]][n[2]][n[1]] = {}
              if n[0] not in DC[n[3]][n[2]][n[1]]:
                DC[n[3]][n[2]][n[1]][n[0]] = '.'
          DC[w][z][y][x] = cube
  return DC

def do(ll,cyc):
  D = {0: {0: dictify(ll)}}
  curr_act=0
  count=0
  while count < cyc:
    D = expand(D)
    curr_act=0
    DC={}
    for w in list(D.keys()):
      DC[w]={}
      for z in list(D[w].keys()):
        DC[w][z]={}
        for y in list(D[w][z].keys()):
          DC[w][z][y]={}
          for x,cube in list(D[w][z][y].items()):
            nn = neighbors([x,y,z,w])
            act=0
            for n in nn:
              try:
                if D[n[3]][n[2]][n[1]][n[0]] == '#':
                  act+=1
              except KeyError:
                pass
            DC[w][z][y][x]=next_state(cube,act)
            if DC[w][z][y][x] == '#':
              curr_act+=1
    D=DC
    count+=1
    print(curr_act)

if __name__ == '__main__':
  ll = """...#..#.
..##.##.
..#.....
....#...
#.##...#
####..##
...##.#.
#.#.#..."""
  rr = []
  for l in ll.splitlines():
    rr.append([c for c in l])
  do(rr, 6)

