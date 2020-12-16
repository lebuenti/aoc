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
  print('rules', *rules, sep='\n')
  print('ticket', ticket, sep='\n')
  print('nearbies', *nearbies, sep='\n')
  not_in_rule = []
  for nearby in nearbies:
    for n in nearby:
      in_rule = False 
      for r in rules:
        if n in r[0] or n in r[1]:
          in_rule = True
          break
      if not in_rule:
        not_in_rule.append(n)  # TODO unique?
  print('not_in_rule', not_in_rule)
  err_rate = 0
  for nir in not_in_rule:
    err_rate+=nir
  return err_rate

with open ('16.in', 'r') as input:
  print("res", do(input.read().splitlines()))

