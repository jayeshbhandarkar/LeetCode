class Solution(object):
    def setZeroes(self, matrix):
        rowsZero = []
        colsZero = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowsZero.append(i)
                    colsZero.append(j)

        for i in range(rows):
            for j in range(cols):
                if i in rowsZero or j in colsZero:
                    matrix[i][j] = 0
        
