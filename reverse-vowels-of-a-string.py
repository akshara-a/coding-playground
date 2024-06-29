# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        i = 0 
        j = len(s_list) - 1 
        vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
        while i < j: 
            if s_list[i] in vowelsList:
                if s_list[j] in vowelsList: 
                    temp = s_list[i] 
                    s_list[i] = s_list[j] 
                    s_list[j] = temp 
                    j -= 1
                    i += 1 
                else: 
                    j -= 1 
            else: 
                i += 1
                    
        result = ''.join(s_list)
        return result
