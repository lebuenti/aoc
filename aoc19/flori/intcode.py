#!/usr/bin/env python3

class IntCode:
  def __init__(self, program):
    self.nn = list(map(int, program.split(',')))
    self.idx = 0

  def __call__(self):
    while 1:
      self.op = str(self.nn[self.idx]).zfill(5)
      opcode = self.op[-2:]
      #print(list(zip(range(len(self.nn)), self.nn)), opcode, idx)

      incr, f = 0, None
      if opcode == "99":
        break
      elif opcode == "01":
        # addition
        a,b = self.pp(2)
        f = self.nn[self.idx+3]
        self.nn[f] = a+b
        incr+=4
      elif opcode == "02":
        # multiplication
        a,b = self.pp(2)
        f = self.nn[self.idx+3]
        self.nn[f] = a*b
        incr+=4
      elif opcode == "03":
        # change to address
        f = self.nn[self.idx+1]
        print('IntCode input', end=': ')
        self.nn[f] = int(input())
        incr+=2
      elif opcode == "04":
        # output at address
        f = self.p(1)
        print('IntCode output:', f)
        incr+=2
      elif opcode == "05":
        # jump-if-true
        a = self.p(1)
        if a != 0:
          b = self.p(2)
          f = self.idx
          self.nn[f] = b
        incr+=3
      elif opcode == "06":
        # jump-if-false
        a = self.p(1)
        if a == 0:
          b = self.p(2)
          f = self.idx
          self.nn[f] = b
        incr+=3
      elif opcode == "07":
        # less than
        a,b = self.pp(2)
        f = self.nn[self.idx+3]
        self.nn[f] = int(a < b)
        incr+=4
      elif opcode == "08":
        # equals
        a,b = self.pp(2)
        f = self.nn[self.idx+3]
        self.nn[f] = int(a == b)
        incr+=4
      else:
        raise Exception("invalid opcode: " + opcode)

      if f is None or f != self.idx:
        self.idx+=incr
      else:
        self.idx = self.nn[self.idx]

    return self.nn


  def pp(self, q):
    return [self.p(i) for i in range(1,q+1)]


  def p(self, i):
    v = self.nn[self.idx+abs(i)]
    return v if self.op[-2-i] == '1' else self.nn[v]


  def __getitem__(self, idx):
    return self.nn[idx]


  def __setitem__(self, idx, v):
    self.nn[idx] = v

