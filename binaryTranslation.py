# Convert 25 into Binary and represent 0 = '@' and 1 = '$'

n = int(input()) 
temp = bin(n) 
converted_value = temp[2:]

result = ""

for i in converted_value:
    if i == '0':
        result += '@' 
    else:
        result += '$' 
        
print(result)
