class Solution(object):
    def repeatedSubstringPattern(self, s):
        answer = (s + s)[1: -1]
        return s in answer
        
