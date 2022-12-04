#!/usr/bin/env python3
with open("input.txt", encoding = 'utf-8') as f:
    lines = f.read().splitlines()

cContains = 0
cOverlaps = 0

for x in lines:
    right, left = x.split(',')
    rFirst, rSecond = right.split('-')
    lFirst, lSecond = left.split('-')

    if (int(rFirst) <= int(lFirst) and int(rSecond) >= int(lSecond)) or (int(lFirst) <= int(rFirst) and int(lSecond) >= int(rSecond)):
        cContains += 1
    if (int(rFirst) <= int(lSecond) and int(rSecond) >= int(lFirst)) or (int(lFirst) <= int(rSecond) and int(lSecond) >= int(rFirst)):
        cOverlaps += 1

print("part1: ", cContains)
print("part2: ", cOverlaps)
