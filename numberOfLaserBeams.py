# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = [] 

        for i in bank:
            count.append(i.count('1'))

        temp = [0] * len(count)
        for i in temp: 
            if i in count: 
                count.remove(i)
                
        output = 0 

        for i in range(len(count)-1):
            output += (count[i] * count[i+1])

        return output
