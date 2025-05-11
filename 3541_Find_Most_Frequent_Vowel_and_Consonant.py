class Solution(object):
    def maxFreqSum(self, s):
        vowels = set("aeiou")
        vowel = consonant = 0
        vowel_dict = {}
        cons_dict = {}
    
        for char in s:
            if char in vowels:
                if char in vowel_dict:
                    vowel_dict[char] += 1
                else:
                    vowel_dict[char] = 1
            else:
                if char in cons_dict:
                    cons_dict[char] += 1
                else:
                    cons_dict[char] = 1
    
        if vowel_dict:
            vowel = max(vowel_dict.values())
            
        if cons_dict:
            consonant = max(cons_dict.values())
    
        return vowel + consonant
