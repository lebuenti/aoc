#!/usr/bin/env python3
with open("input.txt", encoding = 'utf-8') as f:
    ll = [[int (n) for n in r] for r in f.read().splitlines()] #gracias flori ;-)

copy = [ [0]*len(ll[0]) for i in range(len(ll))]
for i in range(0, len(ll)):
    for j in range(0, len(ll[i])):
        copy[i][j] = ll[i][j]

#links
for i in range(1, len(ll) - 1):
    biggest = ll[i][0]
    for j in range(0, len(ll[i]) - 2):
        if biggest < ll[i][j+1]:
            copy[i][j+1] = -1
            biggest = ll[i][j+1]

#rechts
for i in range(1, len(ll) - 1):
    biggest = ll[i][len(ll[i]) - 1]
    for j in range(len(ll[i]) - 1, 1, -1):
        if biggest < ll[i][j-1]:
            copy[i][j-1] = -1
            biggest = ll[i][j-1]

#top
for i in range(1, len(ll[0]) - 1):
    biggest = ll[0][i]
    for j in range(1, len(ll) -1):
        if biggest < ll[j][i]:
            copy[j][i] = -1
            biggest = ll[j][i]

#bottom
for i in range(1, len(ll[0]) - 1):
    biggest = ll[len(ll)-1][i]
    for j in range(len(ll) - 1, 1, -1):
        if biggest < ll[j-1][i]:
            copy[j-1][i] = -1
            biggest = ll[j-1][i]

count = 0
count += len(ll[0]) + len(ll[0])
count += len(ll) + len(ll) - 4

for x in copy:
    count += x.count(-1)

print("part 1: ", count)

scores = []

def count_trees(range_start, range_end, range_step, i, j):
    c1 = 0
    for h in range(range_start, range_end, range_step):
        c1 += 1
        if ll[i][h] >= ll[i][j]:
            break
    return c1


for i in range(0, len(copy)):
    for j in range(0, len(copy[i])):

        if copy[i][j] == -1:
            c1 = 0
            #left
            for h in range(j - 1, -1, -1):
                c1 += 1
                if ll[i][h] >= ll[i][j]:
                    break

            c2 = 0
            #right
            for h in range(j + 1, len(ll[i])):
                c2 += 1
                if ll[i][h] >= ll[i][j]:
                    break

            c3 = 0
            #up
            for k in range(i - 1, -1, -1):
                c3 += 1
                if ll[k][j] >= ll[i][j]:
                    break

            c4 = 0
            #down
            for k in range(i + 1, len(ll)):
                c4 += 1
                if ll[k][j] >= ll[i][j]:
                    break

            scores.append(c1*c2*c3*c4)


print("part 2: ", max(scores))
