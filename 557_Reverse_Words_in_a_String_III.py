class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        result = []

        for word in words:
            result.append(word[::-1])

        return " ".join(result)
        
