n = int(input())

list_of_elements = list(map(int,input().split()))[:n]

#Method - 1
for i in range(len(list_of_elements)-1,-1,-1):
    print(list_of_elements[i],end=" ")

print()
print("-----------------")

# Method - 2
temp = list_of_elements[::-1]
for i in temp:
    print(''.join(str(i)),end=" ")

print()
print("-----------------")

# Method - 3
list_of_elements.reverse()
for i in list_of_elements:
    print(''.join(str(i)),end=" ")
