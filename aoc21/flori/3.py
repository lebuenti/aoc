#!/usr/bin/env python

def dec(lst):
  return int(''.join([str(i) for i in lst]), 2)


def j1(ll):
  steps = len(ll[0])
  gamma = [0] * steps
  epsil = [0] * steps
  for step in range(steps):
    l0 = l1 = 0
    for l in ll:
      if l[step] == '0':
        l0 += 1
      elif l[step] == '1':
        l1 += 1
    if l0 > l1:
      gamma[step] = 0
      epsil[step] = 1
    else:
      gamma[step] = 1
      epsil[step] = 0

  print(dec(gamma) * dec(epsil))


def j2(ll):
  oxy, co2 = [*ll], [*ll]
  for step in range(len(ll[0])):
    if len(co2) <= 1 and len(oxy) <= 1:
      break
    if len(co2) > 1:
      l1 = len([n for n in co2 if n[step] == '1'])
      l0 = len([n for n in co2 if n[step] == '0'])
      co2 = [n for n in co2 if int(n[step]) == int(not (l0 <= l1))]
    if len(oxy) > 1:
      l1 = len([n for n in oxy if n[step] == '1'])
      l0 = len([n for n in oxy if n[step] == '0'])
      oxy = [n for n in oxy if int(n[step]) == int(l1 >= l0)]

  print(dec(oxy) * dec(co2))
  

with open('3.in', 'r') as f:
  ll = f.read().splitlines()
  j1(ll)
  j2(ll)

