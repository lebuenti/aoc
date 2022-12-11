#!/usr/bin/env python3
import sys
sys.setrecursionlimit(9999999)

with open("input.txt", encoding = 'utf-8') as f:
    L = f.read()
    lines = L.strip().splitlines()

def walk_dirs(dir_stack, commands, dirs_sizes):
    if len(commands) == 0:
        return

    cmd = commands.pop()

    if '$ cd' in cmd:
        cd, dir = cmd.split('$ cd ')

        if '.' not in dir:
            if len(dir_stack) > 0:
                dir = dir_stack[-1] + "-" + dir
            dir_stack.append(dir)

            if dir not in dirs_sizes:
                dirs_sizes[dir] = 0
            return walk_dirs(dir_stack, commands, dirs_sizes)
        else:
            dir_stack.pop()
            return walk_dirs(dir_stack, commands, dirs_sizes)

    elif '$' not in cmd and cmd[0].isdigit():
        size, name = cmd.split(" ")
        current_dir = dir_stack[-1]
        dirs_sizes[current_dir] = dirs_sizes[current_dir] + int(size)

    elif '$' not in cmd and 'dir' in cmd:
        d, dir = cmd.split(" ")

    return walk_dirs(dir_stack, commands, dirs_sizes)


def calc(dss):
    for d,s in dss.items():
        if d == '/':
            continue
        dd = d.split('-')[:-1]
        for i in range(len(dd)):
            print(d, dd, i, dd[:i+1])
            dss['-'.join(dd[:i+1])] += s
        print()

#part1
lines.reverse()
dirs_sizes = {}
walk_dirs([], lines, dirs_sizes)

dirs_sizes_sum = dirs_sizes.copy()
calc(dirs_sizes_sum)

print("part1: ", sum([v for v in dirs_sizes_sum.values() if v <= 100000]))


#part2
dirs_sizes_sum_sorted = sorted([v for k,v in dirs_sizes_sum.items() if k != '/'])
for x in dirs_sizes_sum_sorted:
    if (70000000 - (dirs_sizes_sum['/'] - x)) >= 30000000:
        print("part2: ", x)
        break
