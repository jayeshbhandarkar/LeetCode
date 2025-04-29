class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        count, ans, left = 0, 0, 0
        max_val = max(nums)

        for right in range(n):
            if nums[right] == max_val:
                count += 1

            while count >= k:
                ans += n - right
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return ans
