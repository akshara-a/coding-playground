# https://leetcode.com/problems/remove-element/description/ 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = len(nums)
        temp = nums.count(val)
        limit = count - temp

        while(count > limit):
            print(nums)
            if nums[i] == val:
                nums.remove(nums[i])
                count -= 1
            else:
                i += 1
