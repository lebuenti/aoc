def do(ll):
  ss = [[1,1], [3,1], [5,1], [7,1], [1,2]]
  res = None
  for s in ss:
    trees = 0
    d = s[1]
    r = s[0]
    while d < len(ll):
      rp = r % len(ll[d])
      if ll[d][rp] == '#':
        trees += 1
      d += s[1]
      r += s[0]
    if res is None:
      res = trees
    else:
      res *= trees
  return res

with open('3.in', 'r') as input:
  print("res", do(input.read().splitlines()))

