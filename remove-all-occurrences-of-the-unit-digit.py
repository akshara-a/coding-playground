# Skillrack

# Remove all occurrences of the unit digit 

# Example) 

# Input - 480454
# Output - 805 

# Input - 1005201
# Output - 520

N = int(input())

unit_digit = N%10

val = str(N)
temp = []

for i in val:
    if i != str(unit_digit):
        temp.append(i)
 
result = ''.join(temp)

if(len(result) > 0):
    print(int(result))
else:
    print("-1")
