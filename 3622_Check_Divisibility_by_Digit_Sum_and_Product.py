class Solution(object):
    def checkDivisibility(self, n):
        digits = []
        for d in str(n):
            digits.append(int(d))
        
        digit_sum = 0
        for d in digits:
            digit_sum += d
        
        digit_product = 1
        for d in digits:
            digit_product *= d
    
        total = digit_sum + digit_product
        return n % total == 0
        
