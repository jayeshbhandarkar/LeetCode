class Solution(object):
    def soupServings(self, n):
        if n > 5000:
            return 1.0  

        n = (n + 24) // 25 
        memo = {}

        def solve(a, b):
            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1.0

            if b <= 0:
                return 0.0
                
            if (a, b) in memo:
                return memo[(a, b)]

            memo[(a, b)] = 0.25 * (
                solve(a - 4, b) +
                solve(a - 3, b - 1) +
                solve(a - 2, b - 2) +
                solve(a - 1, b - 3)
            )
            
            return memo[(a, b)]

        return solve(n, n)
