class Solution(object):
    def addDigits(self, num):
        
        while num >= 10:
            add = 0
            while num > 0:
                add += num % 10
                num //= 10
            num = add  
            
        return num
