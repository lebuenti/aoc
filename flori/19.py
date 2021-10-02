#!/usr/bin/env python


recc = ["8", "11"]


def matchstr(R, rk, message, m_idx):
  if m_idx >= len(message):
    # exceeded target string
    return -1
  if '"' in R[rk][0][0]:
    # grammar terminal char
    c = R[rk][0][0].strip('"')
    if message[m_idx] == c:
      return c
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


with open('19.in', 'r') as f:
  rules, messages = f.read().split("\n\n")
  mm = messages.split("\n")
  R = {}
  for l in rules.split("\n"):
    sp = l.split(": ")
    R[sp[0]] = [ n.strip().split(" ") for n in sp[1].split(" | ") ]
  for part in range(1, 3):
    if part == 2:
      R["8"] = [["42"], ["42", "8"]]
      R["11"] = [["42", "31"], ["42", "11", "31"]]
    res = 0
    for m in mm:
      res += (matchstr(R, "0", m, 0) == m)
    print("part", part, "matches", res)

