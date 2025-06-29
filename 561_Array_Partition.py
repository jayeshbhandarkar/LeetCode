class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
        
