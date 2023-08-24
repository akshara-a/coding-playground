# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/ 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle) 
        return idx
