# arr = [10, 11, 12]
# [10 + 11 + 12 + (10+11) + (11+12) + (10+11+12)]
# Output = 110

class Solution:

    def sumOfSubarrays(self, arr: List[int]) -> int:

        n = len(arr)

        result = 0

        for i in range(n):
            for j in range(i,n):
                result += sum(arr[i:j+1])

        return result
