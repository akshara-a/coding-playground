n = int(input())

list_of_elements = list(map(int,input().split()))[:n]

# Method - 1 
temp = sorted(list_of_elements)

for i in temp:
    print(''.join(str(i)),end=" ")

print()
print("----------------------")

# Method - 2
positive = []
negative = []

for i in list_of_elements:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

result = negative + positive 

for i in result:
    print(''.join(str(i)),end=" ")
