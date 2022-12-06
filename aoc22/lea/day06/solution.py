#!/usr/bin/env python3
with open("input.txt", encoding = 'utf-8') as f:
    lines = f.read().splitlines()

def solution(stream, number):
    for i in range(0, len(stream)):
        curr = stream[i:i+number]
        multi = False

        for j in range(0, len(curr)):
            if curr.count(curr[j]) > 1:
                    multi = True

        if not multi:
            print(i+number)
            break

print("part1")
solution(lines[0], 4)
print("part2")
solution(lines[0], 14)
