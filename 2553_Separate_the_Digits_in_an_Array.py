class Solution(object):
    def separateDigits(self, nums):
        result = []

        for num in nums:
            for digit in str(num):
                result.append(int(digit))

        return result
        
