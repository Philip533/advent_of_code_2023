import re
f = open("input", "r")
nlines = f.readlines()

rmax = 12
gmax =13
bmax = 14

power = 1
sum = 0
for line in nlines:
    rbig = 1
    gbig = 1
    bbig = 1
    line = line.replace("\n", "")
    num, games = line.split(":")
    num = num.split(" ")[1]
    arr = games.split(";")
    # Loop over each game
    for _ in arr:
        print(_)
        no_space = re.sub(" ", "", _)
        search = re.findall('\d+[a-z]', no_space)
        for l in search:
            if(l[-1] == "r"):
                if(int(l[0:-1]) > rbig):
                    rbig = int(l[0:-1])
            if(l[-1] == "g"):
                if(int(l[0:-1]) > gbig):
                    gbig = int(l[0:-1])
            if(l[-1] == "b"):
                if(int(l[0:-1]) > bbig):
                    bbig = int(l[0:-1])
    power = rbig * gbig * bbig
    print("Game ", num, power)
    sum = sum + power
print(sum)
