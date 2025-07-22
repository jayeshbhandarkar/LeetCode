class Solution(object):
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        max_sum = 0
        curr_sum = 0
        demo = set()
        i = 0

        for j in range(n):
            while nums[j] in demo:
                demo.remove(nums[i])
                curr_sum -= nums[i]
                i += 1

            demo.add(nums[j])
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

        return max_sum
            
