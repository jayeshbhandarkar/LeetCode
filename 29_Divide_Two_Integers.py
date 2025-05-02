class Solution(object):
    def divide(self, dividend, divisor):
        x = 2**31 - 1
        y = -2**31

        if dividend == y and divisor == -1:
            return x

        neg = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while dividend >= divisor:
            temp = divisor
            mult = 1

            while dividend >= (temp << 1):
                temp <<= 1
                mult <<= 1

            dividend -= temp
            res += mult

        return -res if neg else res
