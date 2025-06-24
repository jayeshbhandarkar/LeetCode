class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        if not s:
            return 0

        sign = 1
        i = 0
        ans = 0

        if s[0] == '-':
            sign = -1
            i += 1

        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1

        ans *= sign

        small = -2**31
        large = 2**31 - 1

        if ans < small:
            return small

        if ans > large:
            return large

        return ans
