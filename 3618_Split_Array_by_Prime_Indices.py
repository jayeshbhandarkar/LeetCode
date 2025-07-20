class Solution(object):
    def splitArray(self, nums):
        n = len(nums)

        is_prime = [False, False] + [True] * (n - 2)  
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        sum_A = 0
        sum_B = 0
        for i in range(n):
            if is_prime[i]:
                sum_A += nums[i]
            else:
                sum_B += nums[i]

        return abs(sum_A - sum_B)
