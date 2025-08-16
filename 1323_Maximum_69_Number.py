class Solution(object):
    def maximum69Number (self, num):
        s = list(str(num))

        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break

        return int("".join(s))


"""
class Solution(object):
    def maximum69Number (self, num):
        result = str(num)
        result = result.replace('6', '9', 1)
        return int(result)
"""        
