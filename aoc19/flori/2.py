#!/usr/bin/env python3

from intcode import IntCode

with open('2.in', 'r') as f:
  r = f.read()

for noun in range(0,99+1):
  for verb in range(0,99+1):
    ic = IntCode(r)
    ic[1] = noun
    ic[2] = verb
    ic()
    if ic.nn[0] == 19690720:
      print(100*noun+verb)
      exit()

assert False

