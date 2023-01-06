#!/usr/bin/env python3

import heapq

L = open('15.in').read().splitlines()
AP = 3

def readingorder(a,b):
  return a[1] - b[1] if a[1] != b[1] else a[0] - b[0]

def neighs(xy, excls=None):
  if excls is None:
    excls = []
  x,y = xy
  nn = set()
  for n in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
    if n not in excls:
      nn.add(n)
  return nn

part1 = None
Lbs, Rbs = 3, 200
while 1:
  rounds = 0
  api = AP if part1 is None else (Lbs + Rbs) // 2
  walls = set()
  elves = set()
  goblins = set()
  H = W = -1
  for y in range(len(L)):
    for x in range(len(L[y])):
      if L[y][x] == '#':
        walls.add((x,y))
      elif L[y][x] == 'E':
        elves.add((x,y))
      elif L[y][x] == 'G':
        goblins.add((x,y))
      H = max(H, x + 1)
    W = max(W, x + 1)

  HP = {(x,y): 200 for x,y in (elves | goblins)}
  starting_elves = len(elves)

  while elves and goblins:
    for (y,x) in sorted([(y,x) for x,y in (elves | goblins)]):
      if (x,y) in elves:
        targets = goblins
        friends = elves
        ap = api
      elif (x,y) in goblins:
        targets = elves
        friends = goblins
        ap = AP
      else:
        continue  # unit has died within this round

      if not targets:
        break

      if not (attacks := {pos for pos in neighs((x,y)) if pos in targets}):
        move = None
        for target in targets:
          excl = walls | friends | (targets - {target})
          G = {(x,y): 0}
          seen = set()
          Q = [(abs(x-target[0]) + abs(y-target[1]), 0, (-1,), (x,y))]
          while Q:
            V = heapq.heappop(Q)
            if V in seen:
              continue
            seen.add(V)
            _,g,start,mpos = V
            if mpos != (x,y) and start[0] == -1:
              start = mpos
            if move is not None and G[mpos] > move[1]:
              break
            if mpos == target:
              break
            for npos in neighs(mpos, excl):
              new_g = g + 1
              if npos not in G or new_g <= G[npos]:
                if npos == target:
                  if move is None:
                    move = (start, mpos), new_g
                  elif new_g < move[1]:
                    move = (start, mpos), new_g
                  elif new_g == move[1]:
                    if readingorder(mpos, move[0][1]) < 0:
                      move = (start, mpos), new_g
                    if move[0][1] == mpos and readingorder(start, move[0][0]) < 0:
                      move = (start, mpos), new_g
                G[npos] = new_g
                heapq.heappush(Q, (new_g + abs(npos[0]-target[0]) + abs(npos[1]-target[1]), new_g, start, npos))

        if move is not None:
          # move
          friends.remove((x,y))
          friends.add(move[0][0])
          HP[move[0][0]] = HP[x,y]
          del HP[x,y]

          # moved into attacking range
          attacks = {pos for pos in neighs(move[0][0]) if pos in targets}

      if attacks:
        attacked = sorted((HP[x1,y1], (y1, x1)) for x1,y1 in attacks)[0][1][::-1]
        HP[attacked] -= ap
        if HP[attacked] <= 0:
          del HP[attacked]
          targets.remove(attacked)
    else:
      rounds += 1  # round has completed

  if part1 is None:
    part1 = sum(HP.values()) * rounds
    print(part1)
  else:
    if len(elves) < starting_elves:
      Lbs = api + 1
    else:
      if Lbs == Rbs:
        print(sum(HP.values()) * rounds)
        break
      Rbs = api

