#!/usr/bin/env python3

from intcode import IntCode
from itertools import combinations_with_replacement as comb
import random

I = open('25.in').read()

DIR = ('east','west','north','south')
OPP = ('west','east','south','north')

def oord(ss,end=True):
  nl = "\n" if end else ''
  return [ord(s) for s in ss+nl]

def cchr(ss):
  return ''.join([chr(s) for s in ss])

def isopp(d1,d2):
  return DIR.index(d1) == OPP.index(d2)

ic = IntCode(I)
inputs = []
items = (
  "bowl of rice",
  "astronaut ice cream",
  "whirled peas",
  "ornament",
  "easter egg",
  "tambourine",
  "mutex",
  "mug",
)
NO = ("photons", "molten lava", "escape pod", "giant electromagnet", "infinite loop")
curr = {*items}
combs = [set(c) for c in comb(items, len(items))]
seen = set()
path = []
nx = None
while 1:
  if nx is not None:
    V = nx
    seen.add(V)
    path.append(V)
    _,direction = V
    ic.inputs = oord(direction)

  out = cchr(ic())

  room = out.splitlines()[3].strip('=').strip()
  if room == "Security Checkpoint":
    print(out)
    inp = ""
    while 1:
      if inp == "":
        for item in curr:
          ic.inputs = oord('drop ' + item)
          ic()
        curr = combs.pop()
        for item in curr:
          ic.inputs = oord('take ' + item)
          ic()
        ic.inputs = oord('west')
        asdf = cchr(ic())
        print('1', asdf.strip().splitlines()[6])
        if "You may proceed" in asdf:
          print(asdf)
          input()
      else:
        ic.inputs = oord(inp)
        print(cchr(ic()))
  dd = [(room,d1) for d1 in DIR if f"- {d1}\n" in out]

  ok = False
  for l in out.strip().splitlines():
    if ok:
      if l.startswith('- '):
        if l[2:] not in NO:
          ic.inputs = oord('take ' + l[2:])
          ic()
      else:
        break
    if l == "Items here:":
      ok = True

  #nx = dd[random.randint(0,len(dd)-1)]
  #continue

  opp = None
  for r,d in dd:
    if nx is not None and isopp(direction,d):
      assert opp is None
      opp = r,d
    elif (r,d) not in seen:
      nx = r,d
      break
  else:
    assert opp is not None
    if opp in seen:
      ic.inputs = oord('inv')
      #print(cchr(ic()))
      nx = dd[random.randint(0,len(dd)-1)]
      #break
    else:
      nx = opp

