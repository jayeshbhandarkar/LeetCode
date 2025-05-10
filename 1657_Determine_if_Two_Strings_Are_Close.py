class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}

        for char in word1:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

        for char in word2:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True
        
