class Solution(object):
    def maxCollectedFruits(self, fruits):
        n = len(fruits)

        for i in range(n):
            for j in range(i + 1, n - (i + 1)):
                fruits[i][j] = 0

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], 
                    fruits[i - 1][j], 
                    fruits[i - 1][j + 1] if j + 1 < n else 0 )

        for j in range(n):
            for i in range(j + 1, n - (j + 1)):
                fruits[i][j] = 0

        for j in range(1, n - 1):
            for i in range(j + 1, n):
                fruits[i][j] += max(
                    fruits[i - 1][j - 1], 
                    fruits[i][j - 1], 
                    fruits[i + 1][j - 1] if i + 1 < n else 0 )

        diag = 0
        for i in range(n):
            diag += fruits[i][i]

        total = diag + fruits[-2][-1] + fruits[-1][-2]
        return total
     
