from numpy import lcm
f = open("input", "r")
line_count = 0
direction = ""
pointers = {}
number_of_steps = 0
start = ""

for line in f:
    line = line.strip()

    if(line_count == 0):
        direction = line
        line_count += 1
    elif(line != ""):
        node = line.split(" = ")[0]
        left = line.split(" = ")[1].split(", ")[0]
        right = line.split(" = ")[1].split(", ")[1]
        # Get rid of pesky brackets
        left = left[1:]
        right = right[0:-1]

        pointers[node] = (left, right)

def navigate2():
    direction_number = 0
    list_of_current = []
    end_dict = {}
    steps = 0

    for items in pointers.keys():
        if(items[-1] == 'A'):
            list_of_current.append(items)


    while (len(list_of_current) != len(end_dict.keys())):
        if(direction_number >= len(direction)):
            direction_number = 0
        list_of_current = [pointers[current][direction[direction_number] == 'R'] for current in list_of_current]
        steps += 1
        direction_number += 1
        for current in list_of_current:
            if(current[-1] == 'Z'):
                end_dict[current] = steps
    product = 1

    print(lcm.reduce(list(end_dict.values())))




def navigate():
    steps = 0
    direction_number = 0
    current = 'AAA'

    # End condition
    while (current != 'ZZZ'):
       
        # Must catch loop
        if (direction_number >= len(direction)):
            direction_number = 0
        if (direction[direction_number] == 'L'):
            current = pointers[current][0]
        else:
            current = pointers[current][1]
        steps += 1
        direction_number += 1
        print(steps)

navigate2()

