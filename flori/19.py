#!/usr/bin/env python


recc = ["8", "11"]


def matchstr(R, rk, message, m_idx):
  if m_idx >= len(message):
    # exceeded target string
    return -1
  if isinstance(R[rk], str):
    # grammar terminal char
    if message[m_idx] == R[rk]:
      return R[rk]
    else:
      return -1
  for rr in R[rk]:
    acc = ''
    for rk1 in rr:
      match = matchstr(R, rk1, message, m_idx + len(acc))
      if match == -1:
        acc = ''
        break
      acc += match
      if message.endswith(acc) and m_idx + len(acc) == len(message):
        if rr.index(rk1) == len(rr) - 1 or rk1 in recc:
          return acc
    if acc != '':
      return acc
  return -1


def do(ll, part):
  R = {}
  messages = []
  reading_grammar = True
  for l in ll:
    if l == '':
      reading_grammar = False
    elif reading_grammar:
      split = l.split(': ')
      if split[1] == '"a"' or split[1] == '"b"':
        R[split[0]] = split[1][1]
      else:
        rr = split[1].split(' | ')
        R[split[0]] = []
        for r in rr:
          R[split[0]].append(r.split(' '))
    else:
      messages.append(l)
  if part == 2:
    R["8"] = [["42"], ["42", "8"]]
    R["11"] = [["42", "31"], ["42", "11", "31"]]
  res = 0
  for message in messages:
    res += (matchstr(R, "0", message, 0) == message)
  print("part", part, "matches", res)


for part in range(2):
  with open('19.in', 'r') as f:
    ll = f.read().splitlines()
    do(ll, part + 1)

