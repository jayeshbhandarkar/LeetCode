class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n+1) // 2
        nums_sum = sum(nums)

        missing_num = total - nums_sum
        return missing_num
        
