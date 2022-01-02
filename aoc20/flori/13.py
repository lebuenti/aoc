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
  db = [(i,int(l)) for i,l in enumerate(ll.split(',')) if l != 'x']
  j = db[0][1]
  ts = 0
  for d,b in db[1:]:
    while (ts+d) % b != 0:
      ts += j
    j *= b
  return ts

with open('13.in', 'r') as f:
  ll = f.read().splitlines()

print(do(ll))
print(do2(ll[1]))

