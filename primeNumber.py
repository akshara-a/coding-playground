def prime(n):
    if n > 2: 
        for i in range(2, n//2):
            if n%i == 0: 
                return "Not Prime" 
        return "Prime"
    return "Not Prime"

n = int(input()) 
print(prime(n))
