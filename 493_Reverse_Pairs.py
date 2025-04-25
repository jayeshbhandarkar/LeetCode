import bisect

class Solution(object):
    def reversePairs(self, nums):
        n = len(nums)
        count = 0
        res = []
       
        for i in range(n):
            count += len(res) - bisect.bisect_right(res, 2 * nums[i])
            bisect.insort(res, nums[i])
        
        return count
              
