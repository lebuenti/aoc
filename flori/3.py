def do(ll):
  trees = 0
  d = 1
  r = 3
  while d < len(ll):
    if r > len(ll[d]):
      rp = r % len(ll[d])
    else:
      rp = r
    if ll[d][rp] == '#':
      trees += 1
    d += 1
    r += 3
  return trees
    

with open('3.in', 'r') as input:
  print("res", do(input.read().splitlines()))

