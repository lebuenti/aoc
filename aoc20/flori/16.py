import re

def do(ll):
  rules = []
  parsing = 'rules'
  nearbies = []
  ticket = None
  for l in ll:
    if l == '':
      pass
    elif l == 'your ticket:':
      parsing = 'ticket'
    elif l == 'nearby tickets:':
      parsing = 'nearby'
    elif parsing == 'rules':
      rule = []
      [r11, r12, r21, r22] = re.match(r"^.+: (\d+)-(\d+) or (\d+)-(\d+)$", l).groups()
      rule.append(range(int(r11), int(r12)+1))
      rule.append(range(int(r21), int(r22)+1))
      rules.append(rule)
    elif parsing == 'ticket':
      ticket = list(map(int, l.split(',')))
    elif parsing == 'nearby':
      nearbies.append(list(map(int, l.split(','))))
  not_in_rule = []
  valids = []
  for nearby in nearbies:
    nearby_in_rule = True
    for n in nearby:
      n_in_rule = False 
      for idx,r in enumerate(rules):
        if n in r[0] or n in r[1]:
          n_in_rule = True
      if not n_in_rule:
        not_in_rule.append(n)
        nearby_in_rule = False
    if nearby_in_rule:
      valids.append(nearby)
  err_rate = 0
  for nir in not_in_rule:
    err_rate+=nir
  n2r = [None] * len(rules)
  for idx,n in enumerate(n2r):
    n2r[idx] = []
  for valid in valids:
    for pos,v in enumerate(valid):
      for r_idx,r in enumerate(rules):
        if v not in r[0] and v not in r[1]:
          n2r[r_idx].append(pos)
  allowances = []
  for pos in range(len(ticket)):
    allowed = []
    for idx,r in enumerate(n2r):
      if pos not in r:
        allowed.append(idx);
    allowances.append(allowed)
  res = []
  counter = 0
  while counter < len(allowances):
    least_allowances = None
    for idx,a in enumerate(allowances):
      if len(a) == 0:
        continue
      if least_allowances is None or len(least_allowances[1]) > len(a):
        least_allowances = [idx, [*a]]
    for idx,a in enumerate(allowances):
      if idx == least_allowances[0]:
        assigned = []
        for i in res:
          assigned.append(i[1])
        if least_allowances[1][0] not in assigned:
          res.append([least_allowances[0], least_allowances[1][0]]) 
        else:
          raise Exception("cannot assign rule that's already been assigned to a row")
      idx = None
      try:
        idx = a.index(least_allowances[1][0])
      except ValueError:
        pass
      if idx is not None:
        a.pop(idx)
    counter+=1
  departure_rules = range(6)
  ss = None
  for dep in departure_rules:
    row = None
    for r in res:
      if r[1] == dep:
        if ss is None:
          ss = ticket[r[0]]
        else:
          ss *= ticket[r[0]]
  return ss

with open ('16.in', 'r') as input:
  print("res", do(input.read().splitlines()))

