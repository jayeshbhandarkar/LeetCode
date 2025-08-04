class Solution(object):
    def minRemoval(self, nums, k):
        n = len(nums)
        if n <= 1:
            return 0
            
        nums.sort()
        answer = n
        l = 0
        
        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            answer = min(answer, n - (r - l + 1))
        
        return answer
