#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#Return the absolute difference between the sums of the matrix's two diagonals as a single


def diagonalDifference(arr):
    # Write your code here
    sum_of_left_to_right = 0
    sum_of_right_to_left = 0
    for i in range(len(arr)):
        sum_of_left_to_right += arr[i][i]
        sum_of_right_to_left += arr[i][-(i+1)]
    return abs(sum_of_left_to_right - sum_of_right_to_left)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
