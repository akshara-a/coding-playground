# You’re given a string, you’ve to print additional characters needed to make that string a palindrome.

# A Palindrome is a sequence of characters that has the property of reading the same in either direction.

# Input :
# abede
# Output :
# ba

# Sample Input :
# abcfe

# Sample output :
# fcba

def ispal(s):
    return s == s[::-1]

s = input() 

for i in range(len(s)): 
    x = s[:i][::-1] 
    if ispal(s+x):
        print(x)
        break 
