# Hackerrank
# https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    reverse_s = s[::-1]
    x = []
    y = []
    for i in s:
        x.append(ord(i))
    for i in reverse_s:
        y.append(ord(i))
        
    res_x = []
    res_y = []
    for i in range(len(s)-1):
        res_x.append(abs(x[i]-x[i+1]))
        res_y.append(abs(y[i]-y[i+1]))
    
    if res_x == res_y:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
