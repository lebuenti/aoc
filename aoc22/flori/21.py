#!/usr/bin/env python3

L = open('21.in').read()
ll = L.splitlines()

step = 1000000000000
yell = 0

H = "humn"
for part in (1,2):
  while 1:
    K = {n[0]: [int(x) if x.isdigit() else x for x in n[1].split(' ')] for n in [l.split(": ") for l in ll]}
    if part == 2:
      K[H] = [yell]
      yell += step
    root = "root"
    assert root in K
    S = [root]
    while S:
      v = S.pop()
      if part == 2 and v == root and isinstance(K[v][0], int) and isinstance(K[v][2], int):
        # part 2 might not work on all inputs
        if K[root][0] == K[root][2]:
          print(yell)
          exit()
        else:
          if K[root][0] - K[root][2] < 0:
            # applying smaller yell increases once we've rolled over to negative values
            yell -= step * 2
            step //= 100
            break
      if isinstance(K[v][0], int):
        if v == root:
          break
        # leaf
        assert len(K[v]) == 1
        for key,val in K.items():
          if len(val) == 1:
            assert isinstance(val[0], int)
            continue
          v1,op,v2 = val
          if v1 == v:
            K[key][0] = K[v][0]
          if v2 == v:
            K[key][2] = K[v][0]
          if isinstance(K[key][0], int) and isinstance(K[key][2], int):
            if part == 1:
              K[key] = [int(eval(f"{K[key][0]}{K[key][1]}{K[key][2]}"))]
              S.append(key)
              if key == root:
                break
            else:
              S.append(key)
              if key == root:
                break
              else:
                K[key] = [int(eval(f"{K[key][0]}{K[key][1]}{K[key][2]}"))]
      else:
        S.append(K[v][0])
        S.append(K[v][2])

    if part == 1:
      print(K[root][0])
      break

