def matchstr(R, g, mm, idx, debug=False):
  """Return matched substring, -1 if there's no match."""
  R[g] = R[g]
  if isinstance(R[g], str):
    return R[g] if mm[idx] == R[g] else -1
  for arr in R[g]:
    acc = ''
    for g1 in arr:
      match = matchstr(R, g1, mm, idx+len(acc))
      if match == -1:
        acc = ''
        break
      else:
        acc += match
    if acc != '':
      return acc
  return -1


def check(R, message):
  mm = [m for m in message]
  limit_idx = None
  if len(R["0"]) > 1:
    raise Exception("that's unexpected")
  acc = ''
  for g in R["0"][0]:
    matches = matchstr(R, g, mm, len(acc), True)
    if matches == -1:
      return False
    acc += matches
  return acc == message


def do(ll):
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
  for message in messages:
    res = check(R, message)
    print(res, message)


with open('19.in', 'r') as f:
  ll = f.read().splitlines()
  do(ll)

