# PART1
c1 = 0
curr = 50
with open("1-input.txt", encoding="utf-8") as f:
    for line in f:
        distance = int(line[1:])
        if "L" in line:
            curr = (curr - distance) % 100
        else:
            curr = (curr + distance) % 100
        if curr == 0:
            c1 += 1
print("part1:", c1)

# PART2
curr = 50
c2 = 0
with open("1-input.txt", encoding="utf-8") as f:
    for line in f:
        distance = int(line[1:])

        if "L" in line:
            if curr - distance < 0:
                c2 += abs((100 + curr - distance) // 100)
                if curr != 0:
                    c2 += 1
            curr = (curr - distance) % 100
            if curr == 0:
                c2 += 1
        else:
            c2 += (curr + distance) // 100
            curr = (curr + distance) % 100

print("part2:", c2)
