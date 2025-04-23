class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        
        for char in s:
            if char.isalnum():
                s1 += char.lower()  
    
        return s1 == s1[::-1]
