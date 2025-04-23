class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i  
        
        return -1  
