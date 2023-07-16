# Given a number n, count the number of unset bits (0s).

# Input Format

# The first line contains a single integer t. t test cases follow.
# Each test case contains a single integer, n, in one line
# Constraints
# 2 <= t <= 10^4
# 2 <= n <= 10^8

# Output Format
# t lines, each containing the number of unset bits

# Sample Input 0
# 4
# 10
# 32
# 31
# 28733

# Sample Output 0
# 2
# 5
# 0
# 7

# Method-1
def unsetBitsCount(n):
    convert = str(bin(n))
    temp = convert[2:]
    return temp.count('0')

t = int(input())
for i in range(t):
    n = int(input())
    print(unsetBitsCount(n))

# Method-2
from collections import Counter 

def unsetBitsCount(n):
    convert = str(bin(n))
    temp = convert[2:]
    c = Counter(temp)
    return c['0']

t = int(input())
for i in range(t):
    n = int(input())
    print(unsetBitsCount(n))
