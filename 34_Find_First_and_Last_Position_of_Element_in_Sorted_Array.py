import bisect

class Solution(object):
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        if left < len(nums) and nums[left] == target:
            return [left, right - 1]

        else:
            return [-1, -1]
            
