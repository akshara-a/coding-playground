# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)[2:] 

        return temp.count('1')
