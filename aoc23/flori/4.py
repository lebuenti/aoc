#!/usr/bin/env python3

L = open('4.in').read()
ll = L.splitlines()

C = {}
for l in ll:
  spl = l.split(":")
  card = int(spl[0].split(" ")[-1])
  spl1 = spl[1].split(" | ")
  C[card] = tuple([int(n) for n in spl1[i].split(" ") if n != ""] for i in range(len(spl1)))

sm = 0
cnt = {k: 1 for k in C.keys()}
for card, (wnn, haves) in C.items():
  having = [have for have in haves if have in wnn]
  sm += int(2**(len(having) - 1))
  for v in range(card + 1, card + len(having) + 1):
    cnt[v] += cnt[card]
print(sm)
print(sum(v for v in cnt.values()))

