class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
