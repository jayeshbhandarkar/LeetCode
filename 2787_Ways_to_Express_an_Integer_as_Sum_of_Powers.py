class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10 ** 9 + 7
        powers = []
        k = 1

        while True:
            p = k ** x
            if p > n:
                break

            powers.append(p)
            k += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]
        
