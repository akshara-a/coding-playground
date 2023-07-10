# Find the first and last position of the targeted element

n = int(input())
nums = list(map(int,input().split()))[:n]

target = int(input())

first = 0
for i in range(len(nums)):
    if nums[i] == target:
        first = i
        break
print(first+1)

last = 0        
for i in range(len(nums)):
    if(nums[i] == target):
        last = i
print(last+1)
