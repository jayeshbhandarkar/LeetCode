class Solution(object):
    def addBinary(self, a, b):
        result = int(a, 2) + int(b, 2)
        return bin(result)[2:]
        
