n = int(input())

list_of_elements = list(map(int,input().split()))[:n]

mid_index = len(list_of_elements) // 2

if (len(list_of_elements) % 2 != 0):
    print(list_of_elements[mid_index])
else:
    temp = list_of_elements[mid_index-1] + list_of_elements[mid_index]
    print(temp//2)
