n = int(input())

square_of_n = n ** 2
mod_val = pow(10,len(str(n)))

if(n%mod_val == square_of_n%mod_val):
    print("YES")
else:
    print("NO")
