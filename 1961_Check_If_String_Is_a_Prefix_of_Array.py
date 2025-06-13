class Solution(object):
    def isPrefixString(self, s, words):
        result = ""
        m = len(result)
        n = len(s)

        for word in words:
            result += word

            if result == s:
                return True

            if  m > n:
                return False

        return False
        
