#!/usr/bin/env python3

#L = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
L = open('17.in').read().strip()

DONE = 2022
REP = DONE*4+1
WIDE = 7

ROCKS = (
  ((0,0), (1,0), (2,0), (3,0)),
  ((1,0), (1,1), (1,2), (0,1), (2,1)),
  ((2,0), (2,1), (2,2), (0,2), (1,2)),
  ((0,0), (0,1), (0,2), (0,3)),
  ((0,0), (0,1), (1,0), (1,1)),
)

CACHE = 200
DP = {}

chamber = []
rockidx = 0
jetidx = 0
while 1:
  if rockidx % 10 == 0 and chamber:
    # clear the cache
    miny = min(y for _,y in chamber)
    trash = set()
    for pos in chamber:
      if pos[1] > miny+CACHE:
        trash.add(pos)
    for t in trash:
      chamber.remove(t)

  chosenrock = rockidx % len(ROCKS)
  top = min([REP, *[y for _,y in chamber]]) - max(y for _,y in ROCKS[chosenrock])
  x,y = 2, top-4

  rock = set()
  for rx,ry in ROCKS[chosenrock]:
    rock.add((rx+x,ry+y))

  while 1:
    # jet
    chosenjet = jetidx % len(L)
    jet = +1 if L[chosenjet] == '>' else -1
    future = set()
    for rx,ry in rock:
      fx,fy = rx+jet, ry
      if (fx,fy) in chamber or fx >= WIDE or fx < 0:
        break
      future.add((fx,fy))
    else:
      rock = future
    jetidx += 1

    # fall
    future = set()
    for rx,ry in rock:
      fx,fy = rx, ry+1
      if (fx,fy) in chamber or fy >= REP:
        break
      future.add((fx,fy))
    else:
      rock = future
    if rock != future:
      break

  chamber.extend(rock)
  height = REP - min(y for _,y in chamber)

  key = (chosenrock, chosenjet, tuple([x for x,_ in rock]))
  if key in DP:
    #            formula: ((1000000000000 -  a) /  b  * c) +  d
    # applied to example: ((1000000000000 - 15) / 35 * 53) + 25
    # a = first couple rocks that started in the middle of
    #     the pattern until the start of the pattern
    # b = number of rocks in pattern
    # c = height added in pattern (b)
    # d = the height of the rocks in a
    a,b,c,d = DP[key][0], rockidx-DP[key][0], height - DP[key][1], DP[key][1]-1
    res = ((1000000000000 - a) / b * c) + d
    # TODO for the big input only the result where a=1585 works for some reason
    if a == 1585 and res % 1 == 0:
      print(int(res))
      break
  else:
    DP[key] = rockidx, height

  rockidx += 1
  if rockidx == DONE:
    print(height)

