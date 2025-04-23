class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        t = '1' + s + '1'
        n = len(t)
        pre = 0
        one = 0
        suff = 0
        maxi = 0
        initone = 0
        
        for i in range(1, n - 1):
            initone += (t[i] == '1')
        
        for i in range(1, n - 1):
            if t[i] == '0' and one == 0:
                pre += 1
            elif suff == 0 and t[i] == '1' and pre != 0:
                one += 1
            elif one != 0 and t[i] == '0':
                suff += 1
            elif pre != 0 and one != 0 and suff != 0:
                maxi = max(suff + pre, maxi)
                pre = suff
                one = 1
                suff = 0
        
        if pre != 0 and one != 0 and suff != 0:
            maxi = max(maxi, suff + pre)
        
        return initone + maxi
