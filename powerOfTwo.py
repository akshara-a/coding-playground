# https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0, 1):
            for j in range(0, 32):
                temp = pow(2, j)
                if temp == n:
                    return True 
                if temp > n:
                    return False
