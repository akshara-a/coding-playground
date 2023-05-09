# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

n = int(input())

list_of_elements = []

try:
    for i in range(n):
        val = int(input())
        if (val > 2 or val < 0):
            raise Exception()
        else:
            list_of_elements.append(val)

    list_of_elements.sort()

    for i in list_of_elements:
        print(''.join(str(i)),end=" ")

except:
    print("Invalid input! Only 0, 1, and 2 is allowed")
