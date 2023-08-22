# Problem Statement :

# You have write a function that accepts, a string which length is “len”, the string has some “#”, in it you have to move all the hashes to the front of the string and return the whole string back and print it.

# char* moveHash(char str[],int n);

# Example :
# Sample Test Case
# Input :
# Move#Hash#to#Front
# Output :
# ###MoveHashtoFront

s = input() 
val = s.count('#')
s1 = ""
for i in s: 
    if i.isalpha():
        s1 += i 
print('#'*val, end="")
print(s1)
