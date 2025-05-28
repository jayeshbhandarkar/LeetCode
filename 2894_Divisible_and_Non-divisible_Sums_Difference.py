class Solution(object):
    def differenceOfSums(self, n, m):
        n1 = [num for num in range(1, n + 1) if num % m]
        n2 = [num for num in range(1, n + 1) if not num % m]

        return sum(n1) - sum(n2)
        
