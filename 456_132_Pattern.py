class Solution(object):
    def find132pattern(self, nums):
        mid = float('-inf')
        stack = []

        for n in reversed(nums):
            if n < mid:
                return True

            while stack and stack[-1] < n:
                mid = stack.pop()
            
            stack.append(n)
        
        return False
         
