class Solution(object):
    def coloredCells(self, n):
        if n<2:
            return n

        sum = 1

        for i in range(1, n):
            j = 4*i
            sum = sum + j
        
        return sum
        
