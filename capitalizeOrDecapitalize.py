# You’re given a function that accepts the following, a string1, its length and a character c. Your job is to replace all the occurrences of character c in string1 and capitalize it or decapitalize it based on the character c.

# Input :
# hello world
# l
# Output :
# heLLo worLd

# Input :
# prepinsta
# p
# Output :
# PrePinsta

s = input() 
c = input() 

result = s.replace(c, c.swapcase())
print(result)
