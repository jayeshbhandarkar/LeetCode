# Solution using Backtracking (Recursive Approach)

class Solution(object):
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1) 
                nums[start], nums[i] = nums[i], nums[start]  
    
        result = []
        backtrack(0)
        return result


# Solution using itertools.permutations

"""
from itertools import permutations

class Solution(object):
    def permute(self, nums):
        return list(permutations(nums))
"""
