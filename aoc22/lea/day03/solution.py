#!/usr/bin/env python3
with open("input.txt", encoding = 'utf-8') as f:
    lines = f.read().splitlines()

#part2
sum=0
for i in range(0, len(lines), 3):
    for c in lines[i]:
        if c in lines[i+1] and c in lines[i+2]:
            if c.isupper():
                sum += ord(c) - 38
            else:
                sum += ord(c) - 96
            break
print("part2: ", sum)

#part 1
ll = []
for x in lines:
    res = x[:len(x)//2], x[len(x)//2:]
    ll.append(res)

sum=0
for x in ll:
    for c1 in x[0]:
        if c1 in x[1]:
            if c1.isupper():
                sum += ord(c1) - 38
            else:
                sum += ord(c1) - 96
            break
print("part1: ", sum)
