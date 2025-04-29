class Solution(object):
    def majorityElement(self, nums):
        count = {}
        n = len(nums)
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        maj_count = n // 3
        result = []
        
        for i in count:
            if count[i] > maj_count:
                result.append(i)
        
        return result
