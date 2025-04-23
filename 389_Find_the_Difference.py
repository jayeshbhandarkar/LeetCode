class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for ch in s + t:
            result ^= ord(ch)
        
        # Convert ASCII value back to character
        return chr(result)
