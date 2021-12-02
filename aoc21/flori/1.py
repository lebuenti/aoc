#!/usr/bin/env python

def j1(ll):
  c = 0
  prev = ll[0]
  for l in ll[1:]:
    c += l > prev
    prev = l
  return c


def j2(ll):
  W, c = 3, 0
  for i in range(len(ll)):
    c += sum(ll[i:i+W]) < sum(ll[i+1:i+1+W])
  return c


with open('1.in', 'r') as f:
  ll = [int(i) for i in f.readlines()]
  print('1', j1(ll))
  print('2', j2(ll))

