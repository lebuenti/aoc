#!/usr/bin/env python3

from intcode import IntCode

with open('9.in', 'r') as f:
  r = f.read()

print(IntCode(r,inputs=(1,))()[0])
print(IntCode(r,inputs=(2,))()[0])

