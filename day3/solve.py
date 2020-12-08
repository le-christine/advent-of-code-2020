# https://adventofcode.com/2020/day/3
# part 1
with open ("input.txt") as input:
    inp = [line.rstrip() for line in input]

index = 0
count = 0

for line in inp:
    length = len(line)
    if index >= length:
        index -= length
    if line[index] == "#":
        count += 1
    index += 3

print "solution 1:", count

#part 2

with open('input.txt') as input:
	inp = [line.rstrip() for line in input]

slopes = [(1,1), (3,1), (5, 1), (7, 1), (1, 2)]
total = 1
length = len(inp)

for right,down in slopes:
    index = 0
    n = 0
    count = 0
    while n < length:
        if index >= len(inp[n]):
            index -= len(inp[n])
        if inp[n][index] == '#':
            count += 1
        index += right
        n += down
    total *=  count

print "solution 2:", total
