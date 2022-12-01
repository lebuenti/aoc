#!/usr/bin/env python3

ll = open('1.in','r').read().split("\n\n")
x = sorted(sum([int(n) for n in l.split()]) for l in ll)[::-1][:3]
print(x[0])
print(sum(x))

