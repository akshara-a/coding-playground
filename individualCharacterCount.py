# You’re given a string where multiple characters are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :

# Input :
# aabbbbeeeeffggg

# Output:
# a2b4e4f2g3

# Input :
# abbccccc

# Output:
# ab2c5

s = input() 
val = s+'0'

start = val[0] 
count = 0

for i in range(len(val)):
    if val[i] == start: 
        count += 1 
    else:
        start = val[i]
        print(val[i-1],end="")
        print(count, end="")
        count = 1
