# Smallest Exponent 
# https://www.geeksforgeeks.org/smallest-power-of-2-greater-than-or-equal-to-n/

def smallestExponent(n):
    power = val = 1
    while val <= n:
        val = 2 ** power
        power += 1
    return val
    
t = int(input())
for i in range(t):
    n = int(input())
    print(smallestExponent(n))
