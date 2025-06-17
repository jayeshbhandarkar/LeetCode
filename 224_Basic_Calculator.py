class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        num = 0
        sign = 1  

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1

            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * num
                num = 0
                result *= stack.pop()   
                result += stack.pop() 

        result += sign * num
        return result
