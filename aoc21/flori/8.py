#!/usr/bin/env python

with open('8.in', 'r') as f:
  ll = f.read().splitlines()

K = {2: 1, 4: 4, 3: 7, 7: 8}

c = 0
for l in ll:
  bef, aft = l.split(' | ')
  bef1, aft1 = bef.split(' '), aft.split(' ')

  patt = {}
  for o in K.values():
    for b in bef1:
      if len(b) == 2 and o == 1:
        patt['c'] = [c for c in b]
      elif len(b) == 4 and o == 4:
        patt['b'] = [c for c in b if c not in patt['c']]
      elif len(b) == 3 and o == 7:
        patt['a'] = [c for c in b if c not in patt['c']]
      elif len(b) == 7 and o == 8:
        patt['e'] = [c for c in b if c not in patt['a'] and c not in patt['c'] and c not in patt['b']]

  s = ''
  for a in aft1:
    if len(a) in K:
      win = K[len(a)]
    elif len(a) == 5:  # 3, 5, 2
      if patt['c'][0] in a and patt['c'][1] in a:
        win = 3
      elif (patt['e'][0] in a) + (patt['e'][1] in a) == 2:
        win = 2
      else:
        win = 5
    elif len(a) == 6:  # 0, 6, 9
      if (patt['c'][0] in a) + (patt['c'][1] in a) == 2:
        if (patt['e'][0] in a) + (patt['e'][1] in a) == 2:
          win = 0
        else:
          win = 9
      else:
        win = 6
    s += str(win)
  
  c += int(s)

print(c)

