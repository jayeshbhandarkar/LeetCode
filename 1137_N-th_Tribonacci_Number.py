class Solution(object):
    def tribonacci(self, n):
        if n <= 1:
            return n
        
        a, b, c = 0, 1, 1
    
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c
