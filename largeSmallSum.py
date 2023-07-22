# You are required to implement the following Function def LargeSmallSum(arr). 
# The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second 
# largest largest element from the even positions and second smallest from the odd position of given ‘arr’.

# Assumption:
# All array elements are unique
# Array is 0 indexed.

# NOTE
# Return 0 if array is empty
# Return 0, if array length is 3 or less than 3

# Example:-
# Input
# arr:3 2 1 7 5 4

# Output
# 7

# Explanation

# Second largest among even position elements(1 3 5) is 3
# Second largest among odd position elements is 4
# Thus the output is 3+4 = 7

# Sample Input
# arr:1 8 0 2 3 5 6

# Sample Output
# 8

def largeSmallSum(arr):
    arr.sort() 
    
    if len(arr) <= 3:
        return 0
        
    even_pos = [] 
    odd_pos = []
    
    for i in range(len(arr)):
        if i%2 == 0:
            even_pos.append(arr[i]) 
        else:
            odd_pos.append(arr[i]) 
            
    return (odd_pos[1] + even_pos[len(even_pos)-2])
    
    
arr = list(map(int, input().split()))
print(largeSmallSum(arr))
