class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        result = 0

        for r1 in range(m):
            col = [1] * n
            for r2 in range(r1, m):
                for j in range(n):
                    col[j] &= mat[r2][j]

                cons = 0
                for j in range(n):
                    if col[j] == 1:
                        cons += 1
                        result += cons
                    else:
                        cons = 0

        return result
