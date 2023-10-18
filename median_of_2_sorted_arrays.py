# GeeksforGeeks
# https://practice.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1

#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            arr = array1 + array2 
            arr.sort() 
            if(len(arr)%2 != 0):
                mid = len(arr)//2 
                return arr[mid] 
            else:
                m1 = len(arr)//2
                m2 = m1 - 1 
                val = ((arr[m1]+arr[m2]) / 2)
                if(val/int(val) == 1.0): 
                    return int(val) 
                else:
                    return val


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends
