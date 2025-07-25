class Solution(object):
    def maxSum(self, nums):
        seen = set()
        max_sum = 0 

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])

                if nums[i] > 0:
                    max_sum += nums[i]

        if max_sum == 0:
            return max(seen)

        return max_sum
