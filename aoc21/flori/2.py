#!/usr/bin/env python

with open('2.in', 'r') as f:
  ll = f.readlines()
  d = h = aim = 0
  for dir, num in [l.split(' ') for l in ll]:
    num = int(num)
    if dir == "forward":
      h += num
      d += aim * num
    elif dir == "down":
      aim += num
    elif dir == "up":
      aim -= num
  print(d*h)



