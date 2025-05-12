class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result.insert(0, left_sq)
                left += 1

            else:
                result.insert(0, right_sq)
                right -= 1

        return result
