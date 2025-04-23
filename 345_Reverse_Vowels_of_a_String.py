class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        stack = [ch for ch in s if ch in vowels]
        result = []

        for ch in s:
            if ch in vowels:
                result.append(stack.pop())

            else:
                result.append(ch)

        return"".join(result)
        
