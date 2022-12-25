#!/usr/bin/env python3

L = open('25.in').read()
ll = L.splitlines()

def fromsnafu(l):
  if l.isdigit():
    if int(l) > 4:
      return int(l, 5)
    elif int(l) in (0,1,2):
      return int(l)
  elif l == '-':
    return -1
  elif l == '=':
    return -2
  raise Exception(f"unexpected {l}")

def tosnafu(l):
  ret = ''
  while l > 0:
    l, p = divmod(l + 2, 5)
    ret += '=-012'[p]
  return ret[::-1]

sm = 0
for l in ll:
  dec = 0
  for i, c in enumerate(l[::-1]):
    dec += fromsnafu(c) * max(5**i,1)
  sm += dec

print(tosnafu(sm))

