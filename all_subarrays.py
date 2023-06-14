# All subarrays

lst = list(map(int,input().split()))
sub_list = []

for i in range(len(lst)):
    sub_list.append([lst[i]])
    for j in range(i+1,len(lst)):
        temp = lst[i:j+1]
        sub_list.append(temp)
    
print(sub_list)

# 1 2 3
# [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
