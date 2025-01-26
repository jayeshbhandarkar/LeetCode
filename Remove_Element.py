class Solution(object):
    def removeElement(self, nums, val):
        k = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] 
                k += 1 
    
        return k

s1 = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2

print(s1.removeElement(nums1, val1)) 
print(s1.removeElement(nums2, val2))  
