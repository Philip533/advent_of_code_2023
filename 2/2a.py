import re
f = open("input", "r")
nlines = f.readlines()

rmax = 12
gmax =13
bmax = 14
total_id = 0
for line in nlines:
    bad_game = False
    blue = 0
    red = 0
    green = 0
    line = line.replace("\n", "")
    num, games = line.split(":")
    num = num.split(" ")[1]
    arr = games.split(";")
    # Loop over each game
    for _ in arr:
        print(_)
        red = 0
        blue = 0
        green = 0
        no_space = re.sub(" ", "", _)
        search = re.findall('\d+[a-z]', no_space)
        for l in search:
            print(l)
            if(l[-1] == "r"):
                red = red + int(l[0:-1])
            elif(l[-1] == "b"):
                blue = blue + int(l[0:-1])
            elif(l[-1] == "g"):
                green = green + int(l[0:-1])
        if(red > rmax):
            bad_game = True
        elif(blue > bmax):
            bad_game = True
        elif(green > gmax):
            bad_game = True
    # Entire game good
    if(bad_game == False):
        total_id += int(num)
print(total_id)
