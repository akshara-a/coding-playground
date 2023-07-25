# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        print(s1)
        temp = ""
        for i in s1:
            if i.isalnum():
                temp = temp + i 
        print(temp)
        print(temp[::-1])
        if temp == temp[::-1]:
            return 1 
        return 0
