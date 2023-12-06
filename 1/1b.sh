#!/bin/bash 

# Substitute each instant but account for overlapping words

sed 's/one/o1e/g' input > input_1
sed 's/two/t2o/g' input_1 > input_2
sed 's/three/t3e/g' input_2 > input_3
sed 's/four/f4r/g' input_3 > input_4
sed 's/five/f5e/g' input_4 > input_5
sed 's/six/s6x/g' input_5 > input_6
sed 's/seven/s7n/g' input_6 > input_7
sed 's/eight/e8t/g' input_7 > input_8
sed 's/nine/n9e/g' input_8 > input

sh 1a.sh

