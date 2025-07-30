class Solution(object):
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            if curr < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(curr, curr_max * curr)
            curr_min = min(curr, curr_min * curr)

            result = max(result, curr_max)

        return result
        
