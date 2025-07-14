class Solution(object):
    def countVowelSubstrings(self, word):
        vowels = set('aeiou')
        count = 0

        for i in range(len(word)):
            if word[i] in vowels:
                seen = set()

                for j in range(i, len(word)):
                    if word[j] not in vowels:
                        break

                    seen.add(word[j])

                    if len(seen) == 5:
                        count += 1

        return count
        
