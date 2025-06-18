class Solution(object):
    def divideArray(self, nums, k):
        n = len(nums)
        nums.sort()
        res = []

        for i in range(0, n, 3):
            a1, a2, a3 = nums[i], nums[i + 1], nums[i + 2]

            if a3 - a1 > k:
                return []

            res.append([a1, a2, a3])

        return res
