class Solution(object):
    def countEven(self, num):
        def digitSum(n):
            return sum(int(d) for d in str(n))

        count = 0

        for i in range(1, num + 1):
            if digitSum(i) % 2 == 0:
                count += 1

        return count
        
