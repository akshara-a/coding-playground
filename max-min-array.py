n = int(input())

list_of_elements = list(map(int,input().split()))[:n]

# Method - 1
print("Max elemnet", max(list_of_elements))
print("Min elemnet", min(list_of_elements))

print("-----------------")

# Method - 2
list_of_elements.sort()
print("Max elemnet", list_of_elements[n-1])
print("Min elemnet", list_of_elements[0])
