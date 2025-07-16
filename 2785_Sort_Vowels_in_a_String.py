class Solution(object):
    def sortVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        chars = []
        pos = []

        for i, ch in enumerate(s):
            if ch.lower() in vowels:
                chars.append(ch)
                pos.append(i)

        chars.sort()
        result = list(s)

        for i, ch in zip(pos, chars):
            result[i] = ch

        return ''.join(result)
        
