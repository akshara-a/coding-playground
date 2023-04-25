# Check if all digits of a number is even

# Input -
# 2468

# Output
# YES

# Input
# 2357

# Output
# NO

n = int(input())

flag = 0
for i in str(n):
    if(int(i)%2 != 0):
        flag = 1
        print("NO")
        break
if flag == 0:
    print("YES")
