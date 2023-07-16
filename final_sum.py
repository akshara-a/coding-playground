# Codechef
# https://www.codechef.com/problems/FINALSUM

# Method - 1 (Gives TLE)
t = int(input())

for i in range(t):
    n, q = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    for i in range(q):
        l, r = map(int,input().split())
        for i in range(l-1,r,2):
            a[i] = a[i]+1
        for i in range(l,r,2):
            a[i] = a[i]-1
    print(sum(a))
             
# Method - 2 (Efficient)
t = int(input())

for i in range(t):
    n, q = map(int,input().split())
    a = list(map(int,input().split()))[:n]
    temp = 0
    for i in range(q):
        l, r = map(int,input().split())
        if((r-l+1)%2 != 0):
            temp += 1 
    print(sum(a)+temp)
