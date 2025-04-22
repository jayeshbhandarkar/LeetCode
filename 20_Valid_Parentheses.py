class Solution(object):
    def isValid(self, s):
        stack = []
        pairs ={'(':')', '{':'}', '[':']'}

        for i in s:
            if i in pairs:
                stack.append(i)

            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False

        return len(stack) == 0
        
