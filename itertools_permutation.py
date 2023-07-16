# Hackerrank
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

s, x = map(str, input().split())
val = int(x)

lst = list(permutations(s,val))
temp_lst = []

for i in lst:
    ele = ''.join(i)
    temp_lst.append(ele)

temp_lst.sort()

for i in temp_lst:
    print(i)
