def do(ll):
  for idx,l in enumerate(ll):
    split = ll[idx].split(' ')
    op = split[0]
    if op == 'acc':
      continue
    else:
      arg = split[1].strip()
      mm = [*ll]
      if op == 'jmp':
        mm[idx] = 'nop ' + arg
        res = dodo(mm)
        if res is not None:
          return res
      elif op == 'nop':
        mm[idx] = 'jmp ' + arg
        res = dodo(mm)
        if res is not None:
          return res


def dodo(ll):
  acc = 0
  idx_run = []
  idx = 0
  while idx < len(ll):
    if idx in idx_run:
      return None
    idx_run.append(idx)
    split = ll[idx].split(' ')
    op = split[0]
    arg = int(split[1].strip())
    if op == 'acc':
      acc += arg
      idx+=1
    elif op == 'jmp':
      idx += arg
    elif op == 'nop':
      idx+=1
  return acc

with open('8.in', 'r') as input:
  print("res", do(input.read().splitlines()))

