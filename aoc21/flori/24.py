#!/usr/bin/env python

from collections import defaultdict

with open('24.in', 'r') as f:
  ll = f.read().splitlines()
#ll = """\
#inp w
#mul x 0
#add x z
#mod x 26
#div z 26
#add x 0
#eql x w
#eql x 0
#mul y 0
#add y 25
#mul y x
#add y 1
#mul z y
#mul y 0
#add y w
#add y 15
#mul y x
#add z y
#""".splitlines()


for i in range(9, 0, -1):
  numb = str(i) * 14

  inputs = [int(n) for n in numb]
  input_idx = 0

  VAR = defaultdict(lambda: 0)
  for l in ll:
    op, var1, *var2 = l.split(' ')
    if op == 'inp':
      VAR[var1] = inputs[input_idx]
      input_idx += 1
    else:
      assert len(var2) == 1
      var2p = int(var2[0]) if var2[0][-1].isdigit() else VAR[var2[0]]
      if op == 'add':
        VAR[var1] += var2p
      elif op == 'mul':
        VAR[var1] *= var2p
      elif op == 'div':
        assert not (var2p == 0)
        VAR[var1] //= var2p
      elif op == 'mod':
        assert not (VAR[var1] < 0)
        assert not (var2p <= 0)
        VAR[var1] %= var2p
      elif op == 'eql':
        VAR[var1] = int(VAR[var1] == var2p)
      else:
        raise Exception()

  print(numb, VAR['z'])

  if VAR['z'] == 0:
    break

"""
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y

in order for z to be 0
y has to end up being 0

inp w     inp w     inp w
mul x 0   mul x 0   mul x 0
add x z   add x z   add x z
mod x 26  mod x 26  mod x 26
div z 26  div z 1   div z 1
add x 0   add x 10  add x 11
eql x w   eql x w   eql x w
eql x 0   eql x 0   eql x 0
mul y 0   mul y 0   mul y 0
add y 25  add y 25  add y 25
mul y x   mul y x   mul y x
add y 1   add y 1   add y 1
mul z y   mul z y   mul z y
mul y 0   mul y 0   mul y 0
add y w   add y w   add y w
add y 5   add y 10  add y 1
mul y x   mul y x   mul y x
add z y   add z y   add z y

inp w
mul x 0   x is 0
add x z   x is whatever z is
mod x 26  make x 26 to make it 0 here
div z 26
add x 0
eql x w   x has to eq w
eql x 0   x ends up 0 if it is not 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x   x has to be 0
add z y  either both are 0 or z is negative
"""

