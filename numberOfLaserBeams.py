# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = [] 

        for i in bank:
            count.append(i.count('1'))

        temp = [0] * len(count)
