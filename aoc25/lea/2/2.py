#PART1
with open("2-input.txt") as f:
    ranges = [tuple(map(int, part.split("-"))) for part in f.read().split(",")]

invalids = []

for start, end in ranges:
    for num in range(start, end + 1):
        half = len(str(num)) // 2
        if str(num)[:half] == str(num)[half:]:
            invalids.append(num)

print(invalids)
print(sum(invalids))
