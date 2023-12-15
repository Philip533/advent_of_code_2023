import re
from collections import defaultdict
f = open("input", "r")
# f = open("test", "r")

line = f.read()
line = line.replace("\n", "")
splitline = line.split(",")


def part_1(line):
    total = 0
    for j in range(len(line)):
        term = ord(line[j])
        total += term
        total *= 17
        total = total % 256
    return total


def part_2():
    label_dict = defaultdict(dict)
    for i in range(len(splitline)):
        if(splitline[i][-2] == '='):
            label = splitline[i][0:-2]
            print(label)
            box = splitline[i][-1]
            label_dict[part_1(label)][label] = int(box)
        elif(splitline[i][-1] == '-'):
            label = splitline[i][0:-1]
            print(label)
            label_dict[part_1(label)].pop(label, None)
    return label_dict
total = 0

for i in range(len(splitline)):
    total += part_1(splitline[i])

print("Part 1 total = ", total)

box_dict = part_2()

part2_total = 0
print(box_dict)
for i in box_dict:
    for j,l in enumerate(box_dict[i].values()):
        part2_total += (i+1)*(j+1)*l
print(part2_total)
