class Solution(object):
    def zeroFilledSubarray(self, nums):
        count = 0
        subarray = 0
        
        for num in nums:
            if num == 0:
                subarray += 1
                count += subarray  
            else:
                subarray = 0
                
        return count
