class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 1  

        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                total += i 
                pair = num // i
                
                if i != pair:  
                    total += pair

        return total == num  
