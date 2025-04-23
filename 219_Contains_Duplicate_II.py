class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # Set to store last k elements
        window = set()  
        
        for i, num in enumerate(nums):
            if num in window:
                # Found a duplicate within k distance
                return True  
            
            # Add current number to set
            window.add(num)  
            
            if len(window) > k:  
                # Remove the oldest element in window
                window.remove(nums[i - k])  
        
        # No duplicate found within k distance
        return False  
