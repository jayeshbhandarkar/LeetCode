class Solution(object):
    def grayCode(self, n):
        res = []
        total = 1 << n

        for i in range(total):
            res.append(i ^ (i >> 1))

        return res
       
