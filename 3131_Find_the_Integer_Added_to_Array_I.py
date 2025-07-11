class Solution(object):
    def addedInteger(self, nums1, nums2):
        result = (sum(nums2) - sum(nums1)) // len(nums1)
        return result
        
