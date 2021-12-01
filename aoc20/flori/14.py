import re

def do(ll):
  mask = None
  mem = {}
  for l in ll:
    if l[:4] == "mask":
      mask = [m for m in l[7:]]
    else:
      match = re.match(r"mem\[(\d+)\] = (\d+)", l).groups()
      address = format(int(match[0]), '036b')
      decimal = int(match[1])
      binary = format(decimal, '036b')    
      result = [a for a in address]
      for idx,m in enumerate(mask):
        if m != '0':
          result[idx] = m
      rr = []
      stack = [result]
      while len(stack) > 0:
        s = stack.pop(0)
        sofar = ""
        for r in s:
          if r == 'X':
            stack.append([*[c for c in sofar], "1", *result[len(sofar)+1:]])
            sofar += "0"
          else:
            sofar += r
        rr.append(sofar)
      for r in rr:
        mem[int(r,2)] = decimal
  res = 0
  for m in mem.values():
    res += m
  return res
  

with open('14.in', 'r') as input:
  print("res", do(input.read().splitlines()))

