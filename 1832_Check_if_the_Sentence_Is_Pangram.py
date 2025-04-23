class Solution(object):
    def checkIfPangram(self, sentence):
        sentence = sentence.lower()
        letters = set()

        for char in sentence:
            if char.isalpha():
                letters.add(char)

        return True if len(letters) == 26 else False
       
