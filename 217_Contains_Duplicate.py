class Solution(object):
    def containsDuplicate(self, nums):
        count = {}

        for i in nums:
            if i in count:
                return True
            
            count[i] = 1
            
        return False
        
