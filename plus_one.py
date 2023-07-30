# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = '' 
        for i in digits:
            temp += str(i) 

        add = int(temp) + 1 
        
        result = []
        for i in str(add):
            result.append(int(i)) 

        return result
