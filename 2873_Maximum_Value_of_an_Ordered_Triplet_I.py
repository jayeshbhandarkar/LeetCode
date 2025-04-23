class Solution(object):
    def maximumTripletValue(self, nums):
        maxi = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if i < j and j < k:
                        maxi = max(maxi, (nums[i] - nums[j]) * nums[k])

        return maxi
