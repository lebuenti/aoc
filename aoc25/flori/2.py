#!/usr/bin/env python3

L = open('2.in').read().split(",")
p1, p2 = 0, 0
for f,t in [(x, y) for x,y in [l.split("-") for l in L]]:
  for n in range(int(f), int(t)+1):
    s = str(n)
    for i in range(1, len(s)):
      if s.count(s[:i]) * len(s[:i]) == len(s):
        p2 += n
        break
    if s[:len(s)//2] == s[len(s)//2:]:
      p1 += n
print(p1, p2)

