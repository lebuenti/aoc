#!/usr/bin/env python3

with open("input.txt", encoding = 'utf-8') as f:
    lines = f.read().splitlines()


def part2(ll):
    for i, x in enumerate(ll):
        if (x[2] == 'X'):
            if x[0] == 'A':
                ll[i] = x.replace(x[2], 'Z')
            elif x[0] == 'B':
                ll[i] = x.replace(x[2], 'X')
            else:
                ll[i] = x.replace(x[2], 'Y')
        elif x[2] == 'Y':
            ll[i] = x.replace(x[2], x[0])
        else:
            if x[0] == 'A':
                ll[i] = x.replace(x[2], 'Y')
            elif x[0] == 'B':
                ll[i] = x.replace(x[2], 'Z')
            else:
                ll[i] = x.replace(x[2], 'X')
    part1(ll)


def part1(ll):
    ll = [s.replace('A', '1') for s in ll]
    ll = [s.replace('B', '2') for s in ll]
    ll = [s.replace('C', '3') for s in ll]
    ll = [s.replace('X', '1') for s in ll]
    ll = [s.replace('Y', '2') for s in ll]
    ll = [s.replace('Z', '3') for s in ll]

    counter = 0;

    for x in ll:
        if (int(x[0]) == 3 and int(x[2]) == 1) or (int(x[0]) == 1 and int(x[2]) == 3):
            if int(x[0]) == 3 and int(x[2]) == 1:
                counter+= 6
        else:
            if int(x[2]) - int(x[0]) > 0:
                counter += 6
            elif int(x[2]) - int(x[0]) == 0:
                 counter += 3

        counter += int(x[2])

    print("counter: ", counter);


print("part1: ")
part1(lines)
print("part2: ")
part2(lines)
