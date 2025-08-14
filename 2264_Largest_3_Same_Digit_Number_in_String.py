class Solution(object):
    def largestGoodInteger(self, num):
        n = len(num)
        res = ""

        for i in range(n - 2):
            s = num[i:i+3]

            if s[0] == s[1] == s[2]:
                if s > res:
                    res = s

        return res
        
