class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols -1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            mid_val = matrix[row][col]

            if mid_val == target:
                return True

            elif mid_val <= target:
                left = mid + 1

            else:
                right = mid - 1

        return False
        
