# Input (stdin)

# 10 (No.of sizes)
# 2 3 4 5 6 8 7 6 5 18 (list of sizes)
# 6 (no.of customers)
# Below are the size and price purchased by each customer
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Expected Output

# 200

# Explanation

# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned =  55 + 45 + 40 + 60 = 200

n = int(input())
sizes = list(map(int,input().split()))[:n]

customers = int(input())

sum_val = 0
for i in range(customers):
    size, price = map(int,input().split())
    if size in sizes:
        sum_val += price
        sizes.remove(size)
        
print(sum_val)
