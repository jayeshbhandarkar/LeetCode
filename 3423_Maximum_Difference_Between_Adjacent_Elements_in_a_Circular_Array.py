class Solution(object):
    def maxAdjacentDistance(self, nums):
        n = len(nums)
        ans = abs(nums[-1] - nums[0])

        for i in range(1, n):
            ans = max(ans, abs(nums[i] - nums[i - 1]))

        return ans
        
