# Optimized Approach

class Solution(object):
    def maximumDifference(self, nums):
        mini = nums[0]
        max_diff = -1

        for num in nums[1:]:
            if num > mini:
                max_diff = max(max_diff, num - mini)

            else:
                mini = num

        return max_diff


# Brute Force Approach
"""
class Solution(object):
    def maximumDifference(self, nums):
        n = len(nums)
        max_diff = -1
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    diff = nums[j] - nums[i]
                    max_diff = max(max_diff, diff)

        return max_diff
"""
