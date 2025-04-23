class Solution(object):
    def maxPower(self, s):
        max_count = count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                max_count = max(max_count, count)

            else:
                count = 1

        return max_count       
