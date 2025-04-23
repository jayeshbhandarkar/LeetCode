class Solution(object):
    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0  

        left, right = 1, max(candies)

        while left <= right:
            mid = (left + right) // 2
            total_children = sum(c // mid for c in candies)  

            if total_children >= k:
                left = mid + 1
            else:
                right = mid - 1 

        return right  
