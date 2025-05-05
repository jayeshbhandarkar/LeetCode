class Solution(object):
    def subarraySum(self, nums, k):
        freq = {0: 1}
        curr_sum = 0
        total = 0

        for num in nums:
            curr_sum += num

            if (curr_sum - k) in freq:
                total += freq[curr_sum - k]

            if curr_sum in freq:
                freq[curr_sum] += 1
            else:
                freq[curr_sum] = 1

        return total
        
