class Solution(object):
    def singleNumber(self, nums):
        count = 0

        for i in nums:
            count ^= i 

        return count
        
