class Solution(object):
    def average(self, salary):
        return ((sum(salary) - max(salary) - min(salary)) * 1.0) / (len(salary) - 2)
        
