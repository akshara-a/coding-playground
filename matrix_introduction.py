# Method I love
R = int(input()) 
C = int(input()) 

mat = [] 
for i in range(R):
    temp = list(map(int,input().split()))[:C]
    mat.append(temp) 
    
print(mat)

# Other methods 

# one-liner logic to take input for rows and columns
R = int(input())
C = int(input())
mat = [[int(input()) for x in range (C)] for y in range(R)]
print(mat)

# Numpy package method
import numpy as np 

R = int(input()) 
C = int(input())
entries = list(map(int, input().split()))
 
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)

# Traditional method
R = int(input()) 
C = int(input()) 

mat = []
for i in range(R):
    temp = []
    for j in range(C):
        val = int(input()) 
        temp.append(val)
    mat.append(temp)

print(mat)

