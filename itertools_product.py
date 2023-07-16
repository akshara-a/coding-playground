# Hackerrank
# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

temp = []
temp.append(A)
temp.append(B)

result = list(product(*temp))
print(*result)
