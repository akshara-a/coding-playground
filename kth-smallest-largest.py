n = int(input())

list_of_elements = list(map(int,input().split()))[:n]

k = int(input())

list_of_elements.sort()

# Method - 1
print("kth largest elemnet", list_of_elements[n-k])
print("kth smallest element", list_of_elements[k-1])
