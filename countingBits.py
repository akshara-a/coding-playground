# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            temp = bin(i)[2:]
            val = 0
            for i in temp: 
                val += int(i) 
            result.append(val) 
        return result
