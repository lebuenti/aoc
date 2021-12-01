import re

def do(ll):
  ll.append('')
  req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'
  count = 0
  cache = ''
  for l in ll:
    if l == '':
      valid = True
      for r in req:
        if (' ' + r + ':') not in cache:
          valid = False
          break
      if valid:
        split = cache.split(' ')
        for s in split:
          if s == '':
            continue
          a = s[:3]
          v = s[4:]
          sub_valid = False
          if a == 'byr':
            sub_valid = int(v) >= 1920 and int(v) <= 2002
          elif a == 'iyr':
            sub_valid = int(v) >= 2010 and int(v) <= 2020
          elif a == 'eyr':
            sub_valid = int(v) >= 2020 and int(v) <= 2030
          elif a == 'hgt':
            if v[-2:] == 'cm':
              sub_valid = int(v[:-2]) >= 150 and int(v[:-2]) <= 193
            elif v[-2:] == 'in':
              sub_valid = int(v[:-2]) >= 59 and int(v[:-2]) <= 76
            else:
              sub_valid = False
          elif a == 'hcl':
            sub_valid = re.match(r"^#[0-9a-f]{6}$", v) is not None
          elif a == 'ecl':
            sub_valid = v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
          elif a == 'pid':
            sub_valid = re.match(r"^\d{9}$", v) is not None
          elif a == 'cid':
            sub_valid = True
          if not sub_valid:
            valid = False
            break
      if valid:
        count += 1
      cache = ''
    else:
      cache += ' ' + l
  return count
    

with open('4.in', 'r') as input:
  print("res", do(input.read().splitlines()))

