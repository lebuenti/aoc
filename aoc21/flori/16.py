#!/usr/bin/env python

from math import prod

with open('16.in', 'r') as f:
  inp = f.read().strip()


def meh(d, sub=None):
  c = 0
  idx = 0

  nacc = []
  subcount = 0
  while idx < len(d):
    subcount += 1

    c += int(d[idx:idx+3], 2)
    idx += 3

    t = int(d[idx:idx+3], 2)
    idx += 3

    if t == 4: 
      # literal
      acc = ''
      while True:
        chunk = d[idx:idx+5]
        acc += d[idx+1:idx+5]
        idx += 5
        if chunk[0] == '0':
          break
      nacc.append(int(acc, 2))
    else:
      # operator
      ltid = int(d[idx:idx+1], 2)
      idx += 1
      if ltid == 0:
        leng = int(d[idx:idx+15], 2)
        idx += 15
        _, sub_c, sub_acc = meh(d[idx:idx+leng])
        c += sub_c
        idx += leng
      elif ltid == 1:
        quant = int(d[idx:idx+11], 2)
        idx += 11
        sub_idx, sub_c, sub_acc = meh(d[idx:], quant)
        c += sub_c
        idx += sub_idx
      else:
        raise Exception()

      res = None
      if t == 0:
        res = sum(sub_acc)
      elif t == 1:
        res = prod(sub_acc)
      elif t == 2:
        res = min(sub_acc)
      elif t == 3:
        res = max(sub_acc)
      elif t == 5:
        res = int(sub_acc[0] > sub_acc[1])
      elif t == 6:
        res = int(sub_acc[0] < sub_acc[1])
      elif t == 7:
        res = int(sub_acc[0] == sub_acc[1])
      nacc.append(res)

    if subcount == sub:
      break

  return idx, c, nacc


binstr = ''.join([bin(int(hx,16))[2:].zfill(4) for hx in inp])
_, sumver, evalu = meh(binstr, sub=1)
assert len(evalu) == 1
print(sumver, evalu[0])

