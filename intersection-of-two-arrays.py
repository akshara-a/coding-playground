# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) > len(nums2): 
            for i in nums2: 
                if i in nums1: 
                    result.append(i) 
        else: 
            for i in nums1: 
                if i in nums2: 
                    result.append(i) 

        final_output = [] 
        for i in result: 
            if i not in final_output: 
                final_output.append(i) 

        return final_output
