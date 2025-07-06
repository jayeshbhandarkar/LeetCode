class Solution(object):
    def concatHex36(self, n):
        sq = n * n
        cube = n * n * n

        hex_str = format(sq, 'X')
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        b36 = ''
        
        while cube > 0:
            b36 = chars[cube % 36] + b36
            cube //= 36
            
        if b36 == '':
            b36 = '0'

        return hex_str + b36
        
