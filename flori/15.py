def do():
  ll = [0,5,4,1,10,14,7]; goal = 30000000
  dd = {}
  for idx,l in enumerate(ll):
    dd[l] = [idx+1]
  count = len(ll)
  last = ll[-1]
  while count < goal:
    count+=1
    if last not in dd or len(dd[last]) < 2:
      dd[0] = [dd[0][-1], count]
      last = 0
    else:
      [one, two] = dd[last]
      last = two-one
      if last in dd:
        dd[last] = [dd[last][-1], count]
      else:
        dd[last] = [count]
  print(last)

do()

