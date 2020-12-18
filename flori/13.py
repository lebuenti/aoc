import math

def do(ll):
  ts = int(ll[0])
  bb = list(map(int, filter(lambda x: x != 'x', ll[1].split(','))))
  bus = None
  ww = None
  for b in bb:
    calc = 0
    while calc < ts:
      calc += b
    w = calc-ts
    if bus is None or w < ww:
      ww = w
      bus = b
  return ww * bus

def do2(ll):
  """
  Reading the Subreddit there are two ways to solve this:
  1. Chinese Remainder Problem
  2. Find a pattern to increment t faster
  """
  bb = list(map(lambda x: int(x) if x != 'x' else x, ll[0].split(',')))
  t = bb[0]
  while 1:
    t+=bb[0]
    valid = None
    for idx,b in enumerate(bb):
      if idx == 0 or b == 'x':
        continue
      if ((t+idx)%b) == 0:
        valid = True
      else:
        valid = False
        break
    if valid is None:
      raise Exception()
    if valid is True:
      return t

with open('13.in', 'r') as input:
  """
  print("res", do2(["17,x,13,19"]), 3417)
  print("res", do2(["67,7,59,61"]), 754018)
  print("res", do2(["67,x,7,59,61"]), 779210)
  print("res", do2(["67,7,x,59,61"]), 1261476)
  print("res", do2(["1789,37,47,1889"]), 1202161486)
  """
  print("final :")
  print("res", do2([input.read().splitlines()[1]]))

