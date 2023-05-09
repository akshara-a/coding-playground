n1 = int(input())

arr1_list_of_elements = list(map(int,input().split()))[:n1]

n2 = int(input())

arr2_list_of_elements = list(map(int,input().split()))[:n2]

temp_arr = arr1_list_of_elements + arr2_list_of_elements
temp_arr.sort()

mid_index = len(temp_arr) // 2

if (len(temp_arr) % 2 != 0):
    print(temp_arr[mid_index])
else:
    temp = temp_arr[mid_index-1] + temp_arr[mid_index]
    print(temp//2)
