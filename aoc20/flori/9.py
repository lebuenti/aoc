def sums(nn):
  ss = []
  for idx,n in enumerate(nn):
    for idx1,n1 in enumerate(nn):
      if idx == idx1:
        continue
      ss.append(n + n1)
  return ss


def do(ll):
  res1 = None
  preamble = 25
  nn = list(map(int, ll))
  for idx,n in enumerate(nn):
    if idx >= preamble:
      ss = sums(nn[idx-preamble:idx])
      if n not in ss:
        res1=n
        break
  return do2(nn, res1)


def sum(nn):
  s = 0
  for idx,n in enumerate(nn):
    for idx1,n1 in enumerate(nn):
      if idx == idx1:
        continue
    s += n + n1
  return s 


def do2(nn, weak):
  idx = 0
  for idx,n in enumerate(nn):
    s = n
    a = 1
    rr = [n]
    while s < weak:
      rr.append(nn[idx+a])
      s += nn[idx+a]
      if s == weak:
        rr.sort()
        return rr[0] + rr[-1]
      a+=1

with open('9.in', 'r') as input:
  print("res", do(input.read().splitlines()))

