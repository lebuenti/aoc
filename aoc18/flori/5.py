#!/usr/bin/env python3

L = open('5.in').read().strip()

while 1:
  for i in range(len(L)-1):
    if L[i].lower() == L[i+1].lower() and L[i] != L[i+1]:
      assert (L[i].isupper() and L[i+1].islower()) or (L[i].islower() and  L[i+1].isupper())
      L = L[:i] + L[i+2:]
      break
  else:
    break
print(len(L))

mn = len(L)
for c in 'abcdefghijklmnopqrstuvwxyz':
  J = [j for j in L if j.lower() != c]
  while 1:
    for i in range(len(J)-1):
      if J[i].lower() == J[i+1].lower() and J[i] != J[i+1]:
        assert (J[i].isupper() and J[i+1].islower()) or (J[i].islower() and  J[i+1].isupper())
        J = J[:i] + J[i+2:]
        break
    else:
      break
  mn = min(len(J), mn)
print(mn)

