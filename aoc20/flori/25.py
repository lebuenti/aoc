#!/usr/bin/env python3

PK = 15113849, 4206373
DIV = 20201227

subject_number = 7
v = ls = 1
while 1:
  v *= subject_number
  v %= DIV
  if v == PK[1]:
    v = 1
    subject_number = PK[0]
    for i in range(ls):
      v *= subject_number
      v %= DIV
    print(v)
    exit(0)
  ls += 1

