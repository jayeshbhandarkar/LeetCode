class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        
        while low < high:
            mid = (low + high) // 2  
            
            hours_needed = 0
            for p in piles:
                hours_needed += (p + mid - 1) // mid
            
            if hours_needed > h:
                low = mid + 1
            else:
                high = mid
        
        return low
