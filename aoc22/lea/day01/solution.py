#!/usr/bin/env python
with open("input.txt", encoding = 'utf-8') as f:
    ll = f.read().splitlines()

sums = [];
counter = 0;

for x in ll:
    if not x:
        counter += 1;
    if x:
        if len(sums) <= counter:
            sums.insert(counter, int(x))
        else:
            sums[counter] = sums[counter] + int(x)

##Part 2
biggies = []

for x in range(3):
    print("Max value element : ", max(sums))
    biggies.append(max(sums))
    sums.remove(max(sums))

caloriesBiggies = 0
for x in biggies:
    caloriesBiggies = caloriesBiggies + x

print("Calories from 3 biggest: ", caloriesBiggies)
