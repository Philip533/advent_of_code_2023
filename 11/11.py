import sys
from itertools import combinations
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
f = open("input", "r")

nlines = 0
array = []
row_to_dupe = []
col_to_dupe = []

def find_galaxies(matrix):
    coordinate = []
    for i in range(len(matrix[:,0])):
        for j in range(len(matrix[0,:])):
            if(matrix[i][j] == '#'):
                coordinate.append((i,j))
    return coordinate

def galaxy_col_check(matrix_in):
    linelength = len(matrix_in[0,:])
    for j in range(linelength):
        galaxy_count = 0
        for i in range(nlines):
            if(matrix_in[i,j] == '#'):
                galaxy_count += 1
        if(galaxy_count != 0):
            # print("There are " ,galaxy_count , " galaxies in column ", j)
            pass
        else:
            print("There are no galaxies in column ", j)
            col_to_dupe.append(j)

def galaxy_row_check(matrix_in):
    linelength = len(matrix_in[0,:])
    for i in range(nlines):
        galaxy_count = 0
        for j in range(linelength):
            if(matrix_in[i,j] == '#'):
                galaxy_count += 1
        if(galaxy_count != 0):
            pass
            # print("There are " ,galaxy_count , " galaxies in row ", i)
        else:
            print("There are no galaxies in row ", i)
            # matrix_in = np.insert(matrix_in, i-1, matrix_in[i,:], axis = 0)
            row_to_dupe.append(i)
            print(matrix_in[i,:], "MATIX IN")

def find_distance(coords_1, coords_2):
    return abs(coords_1[0] - coords_2[0]) + abs(coords_1[1] - coords_2[1])
array_big = []

for line in f:
    line = line.replace("\n", "")
    array = [x for x in line]
    array_big.append(array)
    nlines += 1

array_big = np.array(array_big)
linelength = len(array[0])
galaxy_row_check(array_big)
galaxy_col_check(array_big)
print(row_to_dupe)
print(col_to_dupe)

expanded = array_big
count = 0
for i in row_to_dupe:
    empty_arr = np.zeros_like(expanded[0,:])
    empty_arr = "."
    expanded = np.insert(expanded, i+count, empty_arr, axis = 0)
    count += 1
count = 0
for j in col_to_dupe:
    empty_arr = np.zeros_like(expanded[:,0])
    empty_arr = "."
    expanded = np.insert(expanded, j+count, empty_arr, axis = 1)
    count += 1


print(len(expanded[1,:]))
print(len(expanded[:,1]))


coords = find_galaxies(expanded)
sum = 0

for pair in combinations(coords, r = 2):
    sum += find_distance(pair[0], pair[1])
print(sum)
