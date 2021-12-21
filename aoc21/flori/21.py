#!/usr/bin/env python3

p = [1, 6]  # original input
#p = [4, 8]  # example input

s = [0, 0]

WIN = 1000
D = 1

turn = 0
while s[0] < WIN and s[1] < WIN:
  t = turn%2
  dice = [(D+i-1)%100+1 for i in range(3)]
  p[t] = (p[t]+sum(dice)-1)%10+1
  D+=3
  s[t] += p[t]
  print(f"Player {t+1} rolls {dice} and moves to space {p[t]} for a total score of {s[t]}.")
  turn +=1

print(min(s) * (D-1))

