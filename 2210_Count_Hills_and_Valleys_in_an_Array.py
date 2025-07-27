class Solution(object):
    def countHillValley(self, nums):
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                res.append(nums[i])
        
        count = 0
        n = len(res)

        for i in range(1, n - 1):
            if res[i] > res[i - 1] and res[i] > res[i + 1]:
                count += 1  # hill

            elif res[i] < res[i - 1] and res[i] < res[i + 1]:
                count += 1  # valley
        
        return count
