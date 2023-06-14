# String manipulation
# Reverse a String

# Method-1
s = input()
print(s[::-1])

# Method-2
s = input()
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
