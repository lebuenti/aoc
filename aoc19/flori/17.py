#!/usr/bin/env python3

from intcode import IntCode

r = open('17.in', 'r').read().strip()

ic = IntCode(r, [])
out = ic()

G = []

idx = 0
for o in out:
  if len(G) <= idx:
    G.append([])
  if o == 35:
    G[idx].append('#')
  elif o == 46:
    G[idx].append('.')
  elif o == 10:
    idx += 1
  else:
    G[idx].append('^')

if len(G[-1]) == 0:
  G.pop()

sm = 0
for y in range(1, len(G)-1):
  for x in range(1, len(G[y])-1):
    if G[y][x] == '#':
      if G[y-1][x] == '#' \
      and G[y+1][x] == '#' \
      and G[y][x+1] == '#' \
      and G[y][x-1] == '#':
        sm += y*x
print('part1:', sm)

assert r[0] == '1'
r = '2,' + ','.join(r.split(',')[1:])
ic = IntCode(r)

def toic(ss):
  ret = ','.join([str(ord(s)) for s in ss])
  return [int(r) for r in (ret+",10").split(',')]

inputs = [
  'A,B,A,B,C,C,B,A,B,C',
  'L,12,L,6,L,8,R,6',
  'L,8,L,8,R,4,R,6,R,6',
  'L,12,R,6,L,8',
  'n'
]

for inp in inputs:
  ic.inputs = toic(inp)
  out = ic()
print('part2:', out[-1])

