#!/usr/bin/env python3

INP = "523764819"

def do(F, LEN):
  global INP
  inp = [int(n) for n in INP]
  idx1 = inp.index(1)

  # neighbor list where idx is label of cup and value is label of next cup
  NN = [None] * (LEN+1)
  for i in range(len(inp)-1):
    NN[inp[i]] = inp[i+1]
  for i in range(10, LEN):
    NN[i] = i+1
  if LEN > 9:
    NN[inp[-1]] = 10
    NN[LEN] = inp[0]
  else:
    NN[inp[-1]] = inp[0]

  LOW, HIGH = 1, LEN
  curr = inp[0]
  for mv in range(1, F+1):
    pickup = (
      NN[curr],
      NN[NN[curr]],
      NN[NN[NN[curr]]]
    )
    nx = NN[pickup[2]]

    wrap = curr-1 < LOW
    sub = int(not wrap)
    cand = HIGH if wrap else curr
    while cand-sub in pickup:
      sub += 1
      if cand-sub < LOW:
        sub = 0
        cand = HIGH
    dest = cand-sub

    repl = {curr: nx, dest: pickup[0], pickup[2]: NN[dest]}
    for k,v in repl.items():
      NN[k] = v

    curr = nx

  return NN


nn = do(100, 9)
res = [nn[1]]
while len(res) < 8:
  n = nn[res[-1]]
  if n is not None:
    res.append(n)
print(''.join([str(n) for n in res]))

nn = do(10_000_000, 1_000_000)
print(nn[1] * nn[nn[1]])

