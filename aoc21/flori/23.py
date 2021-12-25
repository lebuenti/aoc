#!/usr/bin/env python3

from math import inf

with open('23.in', 'r') as f :
  G = f.read().splitlines()

for g in G:
  print(g)

SLOTS = 'xxxAxBxCxD'

COST = {
  'A':    1,
  'B':   10,
  'C':  100,
  'D': 1000,
}


def done(G):
  for fig in ('A', 'B', 'C', 'D'):
    for y in (2, 3):
      if G[y][SLOTS.index(fig)] != fig:
        return False
  return True

def path_free(G, f, t):
  fx,fy = f; tx,ty = t
  S = [f]
  steps = []
  for posf,post in [(fx,tx), (fy,ty)]:
    steps.append(0 if posf==post else 1 if post > posf else -1)
  while S:
    x,y = S.pop()
    if (x,y) == t:
      return True
    for posx,posy in [(x+steps[0],y), (x+steps[0],y), (x,y+steps[1]), (x,y+steps[1])]:
      if G[posy][posx] == '.':
        S.append((posx,posy))
  return False


def where(pred):
  return [(x,y) for y in range(len(G)) for x in range(len(G[y])) if pred(x,y)]


def change(G, f, t):
  G = [*G]
  fx,fy = f; tx,ty = t
  assert G[ty][tx] == '.'
  assert G[fy][fx].isalpha()
  G[ty] = G[ty][:tx] + G[fy][fx] + G[ty][tx+1:]
  G[fy] = G[fy][:fx] + '.' + G[fy][fx+1:]
  return G

MN = +inf
DP = {}
def move(G, curr_cost):
  global DP, MN

  hashG = str(G)
  if hashG in DP:
    return DP[hashG]

  if done(G):
    MN = min(curr_cost, MN)
    return 0

  figs = where(lambda x,y: G[y][x].isalpha())

  moves = []
  for fig_x,fig_y in figs:
    fig = G[fig_y][fig_x]
    target_x = SLOTS.index(fig)

    if fig_x == target_x:
      if fig_y == 3:
        continue  # already lowest sltxt position
      if fig_y == 2 and G[3][target_x] == fig:
        continue  # already in slot and below as well

    if G[3][target_x] == '.' and path_free(G, (fig_x,fig_y), (target_x,3)):
      # change into bottom
      moves.append(((fig_x,fig_y), (target_x,3)))
    elif G[2][target_x] == '.' and G[3][target_x] == fig and path_free(G, (fig_x,fig_y), (target_x,2)):
      # change into slot above bottom
      moves.append(((fig_x,fig_y), (target_x,2)))
    elif fig_y == 2 or (fig_y == 3 and G[2][fig_x] == '.'):
      # change into hallway
      for cand_x in [1,2,4,6,8,10,11]:
        if path_free(G, (fig_x,fig_y), (cand_x,1)):
          moves.append(((fig_x,fig_y), (cand_x,1)))

  if not moves:
    return +inf

  mn_cost, mn_move = +inf, None
  for f,t in moves:
    fig = G[f[1]][f[0]]
    mv_cost = (abs(f[0]-t[0]) + abs(f[1]-t[1])) * COST[fig]
    new_curr_cost = curr_cost + mv_cost
    if new_curr_cost >= MN:
      continue
    tot_cost = mv_cost + move(change(G, f, t), new_curr_cost)
    if tot_cost < mn_cost:
      mn_cost = tot_cost
      mn_move = (f,t)

  DP[hashG] = mn_cost
  return DP[hashG]


print('res', move(G, 0))

