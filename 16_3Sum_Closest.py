class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        close_sum = float('-inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(close_sum - target):
                    close_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return close_sum
        
