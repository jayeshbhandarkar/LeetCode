class Solution(object):
    def findMaxLength(self, nums):
        count, max_len = 0, 0
        freq = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
        
            if count in freq:
                max_len = max(max_len, i - freq[count])
            else:
                freq[count] = i

        return max_len
