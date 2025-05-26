class Solution(object):
    def hammingWeight(self, n):
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count

"""
class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')    
"""
