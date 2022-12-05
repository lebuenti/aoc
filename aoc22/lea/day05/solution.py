#!/usr/bin/env python3
with open("input2.txt", encoding = 'utf-8') as f:
    lines = f.read().splitlines()

idxCraves = 0;
amountCraves = 0;

for i, x in enumerate(lines):
    if "1" in x and not "move" in x:
        idxCraves = i
        amountCraves = int(x[len(x) - 1])
        break

craves1 = []
craves2 = []
for i in range(0,amountCraves):
    craves1.append([])
    craves2.append([])

for i in range(0, idxCraves):
    for j, c in enumerate(lines[i]):
        if c == "[":
            craves1[int(lines[idxCraves][j]) - 1].append(lines[i][j+1])
            craves2[int(lines[idxCraves][j]) - 1].append(lines[i][j+1])
for i in range(0, len(craves1)):
    craves1[i].reverse()
    craves2[i].reverse()


def part1(idxCraves, lines, craves1):
    for i in range(idxCraves + 2, len(lines)):
        amount, stacks = lines[i].split(" from ")
        amount = amount.replace("move ", "")
        fromS, toS = stacks.split(" to ")
        for j in range(0, int(amount)):
            res = craves1[int(fromS) - 1].pop()
            craves1[int(toS) - 1].append(res)
    return craves1

def part2(idxCraves, lines, craves2):
    for i in range(idxCraves + 2, len(lines)):
        amount, stacks = lines[i].split(" from ")
        amount = amount.replace("move ", "")
        fromS, toS = stacks.split(" to ")
        list = []
        for j in range(0, int(amount)):
            res = craves2[int(fromS) - 1].pop()
            list.append(res)
        list.reverse()
        craves2[int(toS) - 1].extend(list)
    return craves2

craves1 = part1(idxCraves, lines, craves1)
craves2 = part2(idxCraves, lines, craves2)

print("part1: ")
for x in craves1:
    print(x.pop(), end="")
print("")

print("part2: ")
for x in craves2:
    print(x.pop(), end="")
print("")
