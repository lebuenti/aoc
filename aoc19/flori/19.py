#!/usr/bin/env python3

from intcode import IntCode

r = open('19.in').read().strip()
ll = [int(n) for n in r.split(',')]

def do(x,y):
  out,*other = IntCode(r, [x,y])()
  assert not len(other)
  return out

sm = 0
for y in range(50):
  for x in range(50):
    sm += do(x,y)
print(sm)

N = 100-1

def findpre():
  """min y where num of '#' is N + N, x of first '#'"""
  for y in range(10,10**10):
    for x in range(0,10**10):
      if do(x,y):
        cnt = 0
        inc = 0
        while do(x+cnt,y):
          cnt+=1
        if cnt >= 100:
          Y = y+N
          for x1 in range(x,10**10):
            if do(x1,Y):
              PRE = x1
              return Y,PRE
        break

def findsquare(Y,PRE):
  for y in range(Y,10**10):
    for x in range(PRE,10**10):
      if do(x,y):
        if do(x+N,y-N):
          return x,y-N
        break

Y,PRE = findpre()

x,y = findsquare(Y,PRE)
print(x*10000+y)

