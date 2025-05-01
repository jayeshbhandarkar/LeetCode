class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            seen = set()
            target = -nums[i]

            for j in range(i + 1, n):
                comp = target - nums[j]

                if comp in seen:
                    res.add((nums[i], comp, nums[j]))

                seen.add(nums[j])

        return list(res)
                
