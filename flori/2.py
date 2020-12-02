import re

def do(ii):
  valid = 0
  for i in ii:
    [min, max, letter, word] = re.match(r"(\d+)-(\d+) (.): (.*)$", i).groups()
    min = int(min)
    max = int(max)
    occ = len([char for char in word if char == letter])
    if occ >= min and occ <= max:
      valid += 1
  return valid

with open('2.in', 'r') as input:
  print(do(input.read().splitlines()))

