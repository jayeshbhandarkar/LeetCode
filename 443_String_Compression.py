class Solution(object):
    def compress(self, chars):
        compressed = []
        i = 0
        n = len(chars)

        while i < n:
            count = 1
            while i + 1 < n and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            
            compressed.append(chars[i])
            
            if count > 1:
                for digit in str(count):
                    compressed.append(digit)
            
            i += 1

        chars[:] = compressed
        return len(chars)
        
