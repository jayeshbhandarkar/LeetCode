class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = bin(n)[2:].zfill(32)
        return int(result[::-1], 2)
