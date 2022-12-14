#!/usr/bin/env python3

from intcode import IntCode

for part in (1,2):
  icc = [IntCode(open('23.in').read().strip(),[i]) for i in range(50)]

  for i,ic in enumerate(icc):
    assert not len(ic())
    assert not len(ic.inputs)

  def tick(part):
    nat = None
    hist = []
    while 1:
      for ic in icc:
        if len(ic.inputs) == 0:
          if part == 2:
            if all(len(ic1.inputs) == 0 for ic1 in icc):
              if nat is not None:
                if nat[1] in hist:
                  return nat[1]
                hist.append(nat[1])
                assert len(icc[0].inputs) == 0
                icc[0].inputs = list(nat)
                break
          ic.inputs = [-1]
        out = ic()
        for o in range(0,len(out),3):
          dest,X,Y = out[o:o+3]
          if dest == 255:
            nat = X,Y
            if part == 1:
              return Y
          else:
            icc[dest].inputs.append(X)
            icc[dest].inputs.append(Y)

  print(tick(part))

