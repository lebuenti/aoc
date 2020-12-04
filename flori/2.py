import re

def do(ii):
  valid = 0
  for i in ii:
    [p1, p2, letter, word] = re.match(r"(\d+)-(\d+) (.): (.*)$", i).groups()
    p1 = int(p1)
    p2 = int(p2)
    if (word[p1-1] == letter) ^ (word[p2-1] == letter):
      valid += 1
    
  return valid

with open('2.in', 'r') as input:
  print(do(input.read().splitlines()))

