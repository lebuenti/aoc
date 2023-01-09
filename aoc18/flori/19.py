#!/usr/bin/env python3

L = """
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
""".strip()
L = open('19.in').read()
ll = L.splitlines()

# Addition:
def addr(a, b, reg):
  """(add register) stores into register C the result of adding register A and register B."""
  return reg[a] + reg[b]
def addi(a, b, reg):
  """(add immediate) stores into register C the result of adding register A and value B."""
  return reg[a] + b

# Multiplication:
def mulr(a, b, reg):
  """(multiply register) stores into register C the result of multiplying register A and register B."""
  return reg[a] * reg[b]
def muli(a, b, reg):
  """(multiply immediate) stores into register C the result of multiplying register A and value B."""
  return reg[a] * b

# Bitwise AND:
def banr(a, b, reg):
  """(bitwise AND register) stores into register C the result of the bitwise AND of register A and register B."""
  return reg[a] & reg[b]
def bani(a, b, reg):
  """(bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B."""
  return reg[a] & b

# Bitwise OR:
def borr(a, b, reg):
  """(bitwise OR register) stores into register C the result of the bitwise OR of register A and register B."""
  return reg[a] | reg[b]
def bori(a, b, reg):
  """(bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B."""
  return reg[a] | b

# Assignment:
def setr(a, _, reg):
  """(set register) copies the contents of register A into register C. (Input B is ignored.)"""
  return reg[a]
def seti(a, _, reg):
  """(set immediate) stores value A into register C. (Input B is ignored.)"""
  return a

# Greater-than testing:
def gtir(a, b, reg):
  """(greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0."""
  return int(a > reg[b])
def gtri(a, b, reg):
  """(greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0."""
  return int(reg[a] > b)
def gtrr(a, b, reg):
  """(greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0."""
  return int(reg[a] > reg[b])

# Equality testing:
def eqir(a, b, reg):
  """(equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0."""
  return int(a == reg[b])
def eqri(a, b, reg):
  """(equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0."""
  return int(reg[a] == b)
def eqrr(a, b, reg):
  """(equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0."""
  return int(reg[a] == reg[b])

calcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
K = {i: [] for i in range(len(calcs))}
insts = []

for l in ll[1:]:
  op, *params = l.split(' ')
  insts.append((op, *[int(n) for n in params]))

ip = int(ll[0][-1])
reg = [1,0,0,0,0,0]
reg = [0] * 6
while reg[ip] < len(insts):
  op, a, b, c = insts[reg[ip]]
  tmp = locals()[op](a,b,reg)
  reg[c] = tmp
  print(op, a, b, c)
  #print(reg, op)
  reg[ip] += 1
print(reg)

"""
here's a repeating sequence found in part
addr 3 1 1
addi 1 1 1
addi 2 1 2
gtrr 2 4 3
addr 1 3 1
seti 2 8 1
mulr 5 2 3
eqrr 3 4 3
"""

DUNNO = 10551306
R5 = 2
reg = [1, 3+1, 10551306, R5 * DUNNO, DUNNO, R5]
while reg[ip] < len(insts):
  op, a, b, c = insts[reg[ip]]
  reg[c] = locals()[op](a,b,reg)
  if reg[2] == 1:
    reg[0] = reg[0] * 2
    reg[2] = DUNNO
    reg[3] = reg[5] * DUNNO
    #reg = [reg[0], 3, 10551306, reg[5] * DUNNO, DUNNO, reg[5]]
  #if op == 'mulr':
  #  print(reg, op)
  reg[ip] += 1
print(reg)
exit()

"""
[12, 3, 1758552, 10551312, 10551306, 6]

changes at register 0

[1, 3, 5275653, 10551306, 10551306, 2]
[3, 3, 5275654, 10551308, 10551306, 2]

[3, 3, 3517102, 10551306, 10551306, 3]
[6, 3, 3517103, 10551309, 10551306, 3]

[6, 3, 1758551, 10551306, 10551306, 6]
[12, 3, 1758552, 10551312, 10551306, 6]

 3 mulr 5 2 3
 4 eqrr 3 4 3
 6 addi 1 1 1
 7 addr 5 0 0
 8 addi 2 1 2
 9 gtrr 2 4 3
10 addr 1 3 1
 2 seti 1 2 2

from mulr to mulr
[0, 3, 10551306, 10551306, 10551306, 1] mulr
[0, 4, 10551306, 1, 10551306, 1] eqrr
[0, 6, 10551306, 1, 10551306, 1] addr
[1, 7, 10551306, 1, 10551306, 1] addr
[1, 8, 10551307, 1, 10551306, 1] addi
[1, 9, 10551307, 1, 10551306, 1] gtrr
[1, 11, 10551307, 1, 10551306, 1] addr
[1, 12, 10551307, 1, 10551306, 2] addi
[1, 13, 10551307, 0, 10551306, 2] gtrr
[1, 14, 10551307, 0, 10551306, 2] addr
[1, 1, 10551307, 0, 10551306, 2] seti
[1, 2, 1, 0, 10551306, 2] seti
[1, 3, 1, 2, 10551306, 2] mulr

[1, 3, 5275653, 10551306, 10551306, 2] mulr
[1, 4, 5275653, 1, 10551306, 2] eqrr
[1, 6, 5275653, 1, 10551306, 2] addr
[3, 7, 5275653, 1, 10551306, 2] addr
[3, 8, 5275654, 1, 10551306, 2] addi
[3, 9, 5275654, 0, 10551306, 2] gtrr
[3, 10, 5275654, 0, 10551306, 2] addr
[3, 2, 5275654, 0, 10551306, 2] seti
[3, 3, 5275654, 10551308, 10551306, 2] mulr

from mulr to mulr
R2 = ?
R1 = ?
R2 = R2 + 1
R3 = R3 + R5
R4 = 10551306
R5 = ?


changes at other registers

[0, 3, 10551306, 10551306, 10551306, 1]
[1, 3, 1, 2, 10551306, 2]

[12, 3, 10551306, 232128732, 10551306, 22]
[12, 3, 1, 23, 10551306, 23]
"""
k1
