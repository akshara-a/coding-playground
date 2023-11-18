# https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/

from collections import Counter

class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	temp = list(set(arr))
    	result = list((Counter(arr) - Counter(temp)).elements())
    	
    	if len(result) > 0:
    	    pass 
    	else:
    	    result.append(-1) 
    	    
    	result1 = list(set(result)) 
    	result1.sort()
    	return result1
    	
    	    
#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
