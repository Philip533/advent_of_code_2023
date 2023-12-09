from numpy.polynomial.polynomial import Polynomial
import numpy as np
f = open("input", "r")

diff = []
diff2 = []

def fit(array):
    fit = Polynomial.fit(np.arange(len(array)), array, len(array) - 1)
    final_term =  round(fit(len(arr)))
    return final_term

sum = 0
sum_part2 = 0
for line in f:
    test = False
    line = line.replace("\n", "")
    line_split = line.split(" ")
    arr = np.array(line_split)
    arr = arr.astype(int)
    fit(arr)
    sum += fit(arr)

    # Just flip the array to get part 2 :)
    sum_part2 += fit(np.flip(arr))

print(sum)
print(sum_part2)
