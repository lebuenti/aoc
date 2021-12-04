#!/usr/bin/env python

import sys

def bingo(b, draw):
  for row in b:
    bing = True
    for num in row:
      if num not in draw:
        bing = False
        break
    if bing:
      return True
  for col in range(5):
    bing = True
    for row in b:
      if row[col] not in draw:
        bing = False
        break
    if bing:
      return True
  return False


def parseb(slist):
  b = []
  for s in slist:
    b.append([int(r) for r in s.split(' ') if r != ''])
  return b


with open('4.in', 'r') as f:
  ll = f.read().splitlines()
  draw = [int(i) for i in ll[0].split(',')]
  bb = []
  for i in range(2, len(ll), 6):
    bb.append(parseb(ll[i:i+5]))

  for fl in range(2):
    ibingo = []
    for i in range(1, len(draw)):
      subdraw = draw[:i]
      firstfound = False
      for i in range(len(bb)):
        if i in ibingo:
          continue
        b = bb[i]
        if bingo(b, subdraw):
          summ = 0
          for row in b:
            for num in row:
              if num not in subdraw:
                summ += num
          res = summ * subdraw[-1]
          if fl == 0:
            print('first', res)
            firstfound = True
            break
          else:
            ibingo.append(i)
            if len(bb) == len(ibingo):
              res = summ * subdraw[-1]
              print('last', res)
              break
      if firstfound:
       break

