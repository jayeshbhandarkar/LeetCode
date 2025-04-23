class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max = float('-inf')

        for candy in candies:
            if candy > max:
                max = candy

        result = []

        for candy in candies:
            if candy + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)

        return result
    
