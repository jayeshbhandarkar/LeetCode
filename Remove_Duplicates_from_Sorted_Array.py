class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        index = 0  
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i] 
        
        return index + 1

nums = [1, 1, 2]
s1 = Solution()
k = s1.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Modified array:", nums[:k])
