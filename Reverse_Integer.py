class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        negative = x < 0

        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1])

        if negative:
            reversed_x = -reversed_x

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x
