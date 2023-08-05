# https://www.hackerrank.com/challenges/lowest-triangle/problem

# The task is to find the smallest integer height of the triangle 

import math

trianglebase,area = [int(x) for x in input().split()]

triangleheight = (2*area)/trianglebase

print(math.ceil(triangleheight))
