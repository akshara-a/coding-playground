# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        temp = sqrt(x) 
        return floor(temp)
