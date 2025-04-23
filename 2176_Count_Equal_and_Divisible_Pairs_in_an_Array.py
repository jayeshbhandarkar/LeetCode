class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1

        return count
        
