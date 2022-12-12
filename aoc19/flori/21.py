#!/usr/bin/env python3

from intcode import IntCode

ll = open('21.in').read()

def toic(ss):
  ret = ','.join([str(ord(s)) for s in ss])
  return [int(r) for r in (ret+",10").split(',')]

def fromic(nn):
  return ''.join([chr(n) for n in nn])

for mode in ("WALK", "RUN"):
  inputs = [
    "OR A J",
    "AND B J",
    "AND C J",
    "NOT J J",
    "AND D J",
  ]
  if mode == "RUN":
    inputs.extend([
      "OR E T",
      "OR H T",
      "AND T J",
    ])
  parsed = [x for y in [toic(inp) for inp in inputs] for x in y]
  ic = IntCode(ll, [*parsed, *toic(mode)])
  print(ic()[-1])


