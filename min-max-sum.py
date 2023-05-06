# Hackerrank
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example
# arr = [1,3,5,7,9]

# The minimum sum is 16 (1+3+5+7) and the maximum sum is 24 (3+5+7+9). The function prints


# 16 24


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    max_sum = min_sum = 0
    for i in range(1,len(arr)):
        max_sum += arr[i]
    for i in range(0,len(arr)-1):
        min_sum += arr[i]
        
    print(f'{min_sum} {max_sum}')
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
