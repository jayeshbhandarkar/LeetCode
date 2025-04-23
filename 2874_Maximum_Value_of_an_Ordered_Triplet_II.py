class Solution(object):
    def maximumTripletValue(self, nums):
        max_value = 0
        max_diff = 0 
        max_triplet = 0

        for num in nums:
            max_triplet = max(max_triplet, max_diff * num)
            max_diff = max(max_diff, max_value - num)          
            max_value = max(max_value, num)

        return max_triplet
        
