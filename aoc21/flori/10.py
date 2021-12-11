#!/usr/bin/env python

with open('10.in', 'r') as f:
  ll = f.read().splitlines()


P = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,

  '(': 1,
  '[': 2,
  '{': 3,
  '<': 4,
}

A = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}


score = 0
cscores = []

for l in ll:
  red = l
  while True:
    rm = False
    for i in range(0, len(red)-1):
      if red[i] in A and A[red[i]] == red[i+1]:
        red = red[:i] + red[i+2:]
        rm = True
        break
    if not rm:
      break

  corrupt = False
  for i in range(len(red)):
    if red[i] in A.values():
      score += P[red[i]]
      corrupt = True
      break

  if not corrupt:
    tcscore = 0
    for c in red[::-1]:
      tcscore *= 5
      tcscore += P[c]
    cscores.append(tcscore)


print('1', score)

cscores.sort()
print('2', cscores[int(len(cscores)/2)])

