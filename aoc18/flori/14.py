#!/usr/bin/env python3

N = open('14.in').read().strip()
A, B = 3, 7
Ai, Bi = 0, 1
recipes = f"{A}{B}"

part1 = part2 = None
while part1 is None or part2 is None:
  recipes += str(A + B)

  if part1 is None and len(recipes) > int(N) + 10:
    part1 = recipes[int(N):int(N)+10]
    print(part1)

  if part2 is None and N in recipes[-len(N)-1:]:
    part2 = recipes.index(N)
    print(part2)

  A = int(recipes[Ai := (Ai + A + 1) % len(recipes)])
  B = int(recipes[Bi := (Bi + B + 1) % len(recipes)])

