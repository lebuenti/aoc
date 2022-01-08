#!/usr/bin/env python3

class IntCode:
  def __init__(self, program, inputs=None):
    self.nn = list(map(int, program.split(',')))
    self.inputs = None if inputs is None else [*inputs]
    self.idx = 0

  def __call__(self, dd=False):
    out = []

    while 1:
      dd and print()
      dd and print(self.idx)
      self.op = str(self.nn[self.idx]).zfill(5)
      opcode = self.op[-2:]
      dd and print(opcode, list(zip(range(len(self.nn)), self.nn)))

      idx_bef = self.idx
      incr = 0
      if opcode == "99":
        break
      elif opcode == "01":
        # addition
        a,b = self.pp(2)
        self.nn[self.nn[self.idx+3]] = a+b
        incr+=4
      elif opcode == "02":
        # multiplication
        a,b = self.pp(2)
        self.nn[self.nn[self.idx+3]] = a*b
        incr+=4
      elif opcode == "03":
        # change to address
        if self.inputs:
          self.nn[self.nn[self.idx+1]] = self.inputs.pop(0)
        else:
          return out
        incr+=2
      elif opcode == "04":
        # output at address
        out.append(self.p(1))
        incr+=2
      elif opcode == "05":
        # jump-if-true
        a = self.p(1)
        if a != 0:
          self.idx = self.p(2)
        incr+=3
      elif opcode == "06":
        # jump-if-false
        a = self.p(1)
        if a == 0:
          self.idx = self.p(2)
        incr+=3
      elif opcode == "07":
        # less than
        a,b = self.pp(2)
        self.nn[self.nn[self.idx+3]] = int(a < b)
        incr+=4
      elif opcode == "08":
        # equals
        a,b = self.pp(2)
        self.nn[self.nn[self.idx+3]] = int(a == b)
        incr+=4
      else:
        raise Exception("invalid opcode: " + opcode)

      if idx_bef == self.idx:
        self.idx += incr

    return out


  def pp(self, q):
    return [self.p(i) for i in range(1,q+1)]


  def p(self, i):
    v = self.nn[self.idx+abs(i)]
    return v if self.op[-2-i] == '1' else self.nn[v]


  def done(self):
    res = self.nn[self.idx] == 99
    if res:
      assert self.op[-2:] == "99"
    return res


  def __getitem__(self, idx):
    return self.nn[idx]


  def __setitem__(self, idx, v):
    self.nn[idx] = v

  def __repr__(self):
    return ','.join(map(str, self.nn))

