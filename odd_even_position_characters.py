# Skillrack
# The program must accept a string value S as the input. The program must print the characters
# which are present at the odd positions if the count of vowels in S is odd. Else, the program
# must print the characters which are present at the even positions as the output. If there is
# no vowel in the string S then the program must print -1 as the output

def result(s,vowels):
    v_count = 0
    for i in s:
        if i in vowels:
            v_count += 1
    
    resultant = ''
    if v_count == 0:
        return -1
    elif v_count%2 == 0:
        for i in range(1, len(s), 2):
            resultant = resultant + s[i]
        return resultant
    else:
        for i in range(0, len(s), 2):
            resultant = resultant + s[i]
        return resultant
            
    
vowels = 'aeiou'
s = input()
print(result(s,vowels))
