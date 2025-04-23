class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        primes = [True] * n  
        primes[0] = primes[1] = False  

        for i in range(2, int(n ** 0.5) + 1):  
            if primes[i]:  
                for multiple in range(i * i, n, i):  
                    primes[multiple] = False  

        return sum(primes)
        
