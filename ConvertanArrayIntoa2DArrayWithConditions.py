# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        container = [] 
        length = len(nums) 
                
        while length != 0:
            temp = []
            track = []
            for i in nums: 
                if i not in temp: 
                    temp.append(i) 
                    track.append(i) 
            for i in track: 
                if i in nums: 
                    nums.remove(i) 
            container.append(temp) 
            length = len(nums) 
        
        return container
