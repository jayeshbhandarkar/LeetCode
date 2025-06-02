class Solution(object):
    def distributeCandies(self, n, limit):
        result = 0
        for i in range(0, limit+1):
            for j in range(0, min(limit, n-i)+1):
                if n-i-j <= limit:
                    result += 1

        return result
        
