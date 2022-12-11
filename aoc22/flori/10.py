#!/usr/bin/env python3

ll = open('10.in').read().splitlines()

def signal():
  return cyc * X if cyc in C else 0

def draw():
  global crt
  crt += '#' if cyc % WIDTH in (X-1, X, X+1) else ' '

C = (20, 60, 100, 140, 180, 220)
WIDTH,HEIGHT = 40, 6
crt = ''
cyc, X = 0, 1
sm = 0
for l in ll:
  check = 0
  draw()
  cyc += 1
  check += signal()
  if l != "noop":
    draw()
    cyc += 1
    check += signal()
    X += int(l.split(" ")[1])
  sm += check

print(sm)
for i in range(0,len(crt),40):
  print(crt[i:i+40])

