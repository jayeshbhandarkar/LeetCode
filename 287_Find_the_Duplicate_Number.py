class Solution(object):
    def findDuplicate(self, nums):
        x = nums[0]
        y = nums[0]

        while True:
            x = nums[x]
            y = nums[nums[y]]

            if x == y:
                break

        x = nums[0]
        
        while x != y:
            x = nums[x]
            y = nums[y]

        return x
        
