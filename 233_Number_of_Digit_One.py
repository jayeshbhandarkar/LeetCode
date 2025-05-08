class Solution(object):
    def countDigitOne(self, n):
        if n <= 0:
            return 0

        count = 0
        factor = 1

        while factor <= n:
            low = n - (n // factor) * factor
            curr = (n // factor) % 10
            high = n // (factor * 10)

            if curr == 0:
                count += high * factor
            elif curr == 1:
                count += high * factor + low + 1
            else:
                count += (high + 1) * factor

            factor *= 10

        return count
