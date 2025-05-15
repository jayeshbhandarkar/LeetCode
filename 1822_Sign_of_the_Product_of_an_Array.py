class Solution(object):
    def arraySign(self, nums):
        product = 1

        for x in nums:
            if x == 0:
                return 0

            elif x < 0:
                product *= -1

        return 1 if product > 0 else -1
        
