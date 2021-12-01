import math


def lower(b):
  return [b[0], math.floor(b[0] + ((b[1] - b[0]) / 2))]


def upper(b):
  return [math.ceil(b[1] - ((b[1] - b[0]) / 2)), b[1]]


def half(char, b):
  if char == 'F' or char == 'L':
    return lower(b)
  if char == 'B' or char == 'R':
    return upper(b)
  raise Exception("no handler: " + char)

  
def do(ll):
  highest = 0
  ids = []
  for l in ll:
    b = [0, 127]
    for char in l[:7]:
      b = half(char, b)
    if b[0] != b[1]:
      raise Exception("%d is not %d" % (b[0], b[1]))
    row = b[0]
    b = [0, 7]
    for char in l[7:]:
      b = half(char, b)
    if b[0] != b[1]:
      raise Exception("%d is not %d" % (b[0], b[1]))
    column = b[0]
    id = row * 8 + column
    if id > highest:
      highest = id
    ids.append(id)
  ids.sort()
  prev = ids[0] 
  for curr in ids[1:]:
    if curr - prev != 1:
      print("yours:", curr-1)
    prev = curr
  return highest


with open('5.in', 'r') as input:
  print("res", do(input.read().splitlines()))

