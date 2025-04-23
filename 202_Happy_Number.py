class Solution(object):
    def isHappy(self, n):
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            
            for digit in str(n):
                total += int(digit) ** 2
            
            n = total
        
        return n == 1 
