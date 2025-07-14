class Solution(object):
    def processStr(self, s):
        answer = []

        for ch in s:
            if ch.islower():
                answer.append(ch)
            elif ch == '*':
                if answer:
                    answer.pop()
            elif ch == '#':
                answer += answer
            elif ch == '%':
                answer.reverse()

        return ''.join(answer)
        
