class Solution(object):
    def countVowels(self, word):
        count = 0
        n = len(word)

        for i in range(n):
            if word[i] in 'aeiou':
                count += (n - i) * (i + 1)

        return count
        
