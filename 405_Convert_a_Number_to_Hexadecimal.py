class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        hex_digits = "0123456789abcdef"
        result = ""

        if num < 0:
            num += 2**32

        while num > 0:
            result = hex_digits[num % 16] + result
            num //= 16

        return result
