class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                length = 1

                while curr + 1 in num_set:
                    curr += 1
                    length += 1

                max_len = max(max_len, length)

        return max_len
        
