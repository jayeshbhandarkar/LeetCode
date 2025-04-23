class Solution(object):
    def minCapability(self, nums, k):
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            i = 0

            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1 
            
            if count >= k:
                right = mid
            else:
                left = mid + 1
        
        return left  
