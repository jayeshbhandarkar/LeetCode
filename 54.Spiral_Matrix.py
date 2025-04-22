class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        top = 0
        bottom = len(matrix) - 1      
        left = 0
        right = len(matrix[0]) - 1  

        while top <= bottom and left <= right:
            # Top Row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Right Column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Bottom Row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Left Column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
