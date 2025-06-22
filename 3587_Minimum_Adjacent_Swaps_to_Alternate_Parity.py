class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        e = [i for i, x in enumerate(nums) if x % 2 == 0]
        o = [i for i, x in enumerate(nums) if x % 2 == 1]
        
        if abs(len(e) - len(o)) > 1:
            return -1
    
        def swaps(pos):
            return sum(abs(i - t) for i, t in zip(pos, range(0, n, 2)))
    
        if len(e) == len(o):
            return min(swaps(e), swaps(o))
        elif len(e) > len(o):
            return swaps(e)
        else:
            return swaps(o)
        
