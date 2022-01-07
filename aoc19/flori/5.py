#!/usr/bin/env python3

from intcode import IntCode

with open('5.in', 'r') as f:
  r = f.read()

IntCode(r)()

