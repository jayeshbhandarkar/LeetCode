class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        
        return count
        
