class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True

        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1 
            if i == len(s): 
                return True
        
        return False  
