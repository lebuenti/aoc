def do(ll):
  res = 0
  ll.append('')
  cache = []
  for l in ll:
    if l == '':
      print(cache)
      for char in cache[0]:
        all = True
        for c in cache[1:]:
          if char not in c:
            all = False
        if all:
          res += 1
      cache = []
    else:
      cache.append([c for c in l])
  return res

with open('6.in', 'r') as input:
  print("res", do(input.read().splitlines()))

