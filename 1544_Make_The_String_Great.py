class Solution(object):
    def makeGood(self, s):
        n = len(s)
        stack = []

        for i in range(n):
            if stack and stack[-1] == s[i].swapcase():
                stack.pop()

            else:
                stack.append(s[i])

        return ''.join(stack)
