class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        powers = []
        bit = 1
        
        while n > 0:
            if n & 1:
                powers.append(bit)
            bit <<= 1
            n >>= 1
        
        result = []
        for left, right in queries:
            prod = 1
            for i in range(left, right + 1): 
                prod *= powers[i]
            result.append(prod % MOD) 
        
        return result
