n1 = int(input())

arr1_list_of_elements = list(map(int,input().split()))[:n1]

n2 = int(input())

arr2_list_of_elements = list(map(int,input().split()))[:n2]

temp_union = arr1_list_of_elements + arr2_list_of_elements

union = set(temp_union)
intersection = intersection = set(arr1_list_of_elements) & set(arr2_list_of_elements)

print(len(union))
print(len(intersection))
