# Characters at multiples of x - reverse

# Example)
# Input - 
# skillrack
# 3

# Output
# kri

s = input().strip()
n = int(input())

for i in range(len(s)-1,0,-n):
    print(s[i],end="")
