# Given a number n, count the number of set bits.

# Input Format
# The first line contains a single integer t. t test cases follow.
# Each test case contains a single integer, n, in one line

# Constraints
# 2 <= t <= 10^4
# 2 <= n <= 10^4

# Output Format
# t lines, each containing the number of set bits

# Sample Input 0
# 4
# 10
# 32
# 31
# 28733

# Sample Output 0
# 2
# 1
# 5
# 8

def setBitsCount(n):
    convert = str(bin(n))
    temp = convert[2:]
    return temp.count('1')

t = int(input())
for i in range(t):
    n = int(input())
    print(setBitsCount(n))
