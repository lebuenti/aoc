#!/usr/bin/env python3

import json

L = open('16.in').read()
B = L.split("\n\n\n")
B1 = B[0].split("\n\n")

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

sm = 0
for b in B1:
  ll = b.splitlines()
  bef = json.loads(ll[0].split(': ')[1])
  opcode, a, b, c = [int(n) for n in ll[1].split(' ')]
  aft = json.loads(ll[2].split(': ')[1])
  sm += sum(aft[c] == calc(a, b, bef) for calc in calcs) >= 3
  for i,calc in enumerate(calcs):
    if aft[c] == calc(a, b, bef):
      if opcode not in K[i]:
        K[i].append(opcode)
print(sm)

cleansed = []
while any(len(v) != 1 for v in K.values()):
  for k,v in K.items():
    if len(v) == 1 and v[0] not in cleansed:
      for k1,v1 in K.items():
        if k1 == k:
          continue
        if v[0] in v1:
          K[k1].remove(v[0])
      cleansed.append(v[0])
      break
assert len(K) == len(set(x for y in K.values() for x in y))

OP = {v[0]: k for k,v in K.items()}
reg = [0] * 4
for cmd in B[-1][1:].splitlines():
  opcode, a, b, c = [int(n) for n in cmd.split(' ')]
  reg[c] = calcs[OP[opcode]](a, b, reg)
print(reg)

