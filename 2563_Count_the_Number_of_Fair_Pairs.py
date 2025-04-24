import bisect

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            min_val = lower - nums[i]
            max_val = upper - nums[i]

            left = bisect.bisect_left(nums, min_val, i+1)
            right = bisect.bisect_right(nums, max_val, i+1)

            res += right - left

        return res
        
