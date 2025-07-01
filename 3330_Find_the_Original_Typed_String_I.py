class Solution(object):
    def possibleStringCount(self, word):
        n = len(word)
        count = 1
        ans = 1
        ch = word[0]

        for i in range(1, n):
            if word[i] == ch:
                count += 1

            else:
                ans += (count - 1)
                ch = word[i]
                count = 1

        ans += (count - 1)
        return ans
