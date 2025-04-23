class Solution(object):
    def findGCD(self, nums):
        x = min(nums)
        y = max(nums)

        return self.gcd(x, y)

    def gcd(self, x, y):
        while y:
            x, y = y, x % y

        return x
        
