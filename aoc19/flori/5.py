#!/usr/bin/env python3

from intcode import IntCode

with open('5.in', 'r') as f:
  r = f.read()

print(IntCode(r, inputs=(1,))()[-1])
print(IntCode(r, inputs=(5,))()[-1])

