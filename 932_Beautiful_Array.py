class Solution(object):
    def beautifulArray(self, n):
        if n == 1:
            return [1]

        elif n == 2:
            return [1, 2]

        odd = self.beautifulArray((n + 1) // 2)
        even = self.beautifulArray((n // 2))

        odd = [2 * x - 1 for x in odd]
        even = [2 * x for x in even]

        return odd + even
        
