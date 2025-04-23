class Solution(object):
    def findMissingAndRepeatedValues(self, grid):

        n = len(grid)
        nums = set()
        total = n * n
        repeated = missing = -1
        
        for row in grid:
            for num in row:
                if num in nums:
                    repeated = num
                nums.add(num)
        
        for i in range(1, total + 1):
            if i not in nums:
                missing = i
                break
        
        return [repeated, missing]  
       
