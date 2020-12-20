def calculate(calc):
  """
  right to left
  """
  init=False
  res=0
  num=''
  operand=None
  for idx,c in enumerate(calc):
    isinit=None
    try:
      int(c)
      isint=True
    except ValueError:
      isint=False
    if isint:
      num+=c
    if not isint or (idx+1) == len(calc):
      if init:
        if operand == '*':
          res*=int(num)
        elif operand == '+':
          res+=int(num)
        else:
          raise Excetion("Unhandled operand: " + c)
        num=''
        operand=c
      else:
        res=int(num)
        num=''
        init=True
        operand=c
  return res

def calculate2(calc):
  """
  left to right addition before multiplication
  """
  S = []
  num=''
  for c in calc:
    isinit=None
    try:
      int(c)
      isint=True
    except ValueError:
      isint=False
    if isint:
      num+=c
    else:
      S.append(num)
      S.append(c)
      num=''
  S.append(num)
  while '+' in S:
    idx=S.index('+')
    sum=int(S[idx-1])+int(S[idx+1])
    S=[*S[:idx-1],sum,*S[idx+2:]]
  res=None
  for s in S:
    if s != '*':
      if res is None:
        res = int(s)
      else:
        res*=int(s)
  return res

def repl(inp):
  opening=None
  for idx,t in enumerate(inp):
    if t in ['(', ')']:
      if t == '(':
        opening=idx
      elif t == ')':
        res=calculate2(inp[(opening+1):idx])
        return "".join([*inp[:opening], str(res), *inp[idx+1:]])

def do(inp):
  inp = inp.replace(" ", "")
  curr = inp
  new_inp=inp
  while '(' in new_inp:
    new_inp=repl(new_inp)
  return calculate2(new_inp)
  
with open('18.in', 'r') as f:
  ll = f.read().splitlines()
  res=0
  for l in ll:
    res+=do(l)

