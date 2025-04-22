class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_length = 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            max_length = max(max_length, i - start + 1)

        return max_length
