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
    print(b, calc, calc-ts)
    if bus is None or w < ww:
      ww = w
      bus = b
  print('bus', bus, ww)
  return ww * bus

def do2(ll):
  bb = list(map(lambda x: int(x) if x != 'x' else x, ll[0].split(',')))
  #print('bb', bb)
  #print()
  #print(bb[0])
  t = bb[0] * 8993524429
  while 1:
    t+=bb[0]
    print(t)
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


"""
print('ts', ts)
print('bb', bb)
bus = None
smallest = None
for idx,b in enumerate(bb):
  res = ts/b
  if smallest is None or res < smallest:
    smallest = res
    bus = b
print('bus', bus)
print('waiting', (bus * math.ceil(smallest)))
print('smallest', smallest)
return ((bus * math.ceil(smallest)) - ts) * bus
"""

