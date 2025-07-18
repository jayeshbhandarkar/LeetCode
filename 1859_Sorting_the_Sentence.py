class Solution:
    def sortSentence(self, s):
        # Reverse the string and then split into words
        words = s[::-1].split()
        
        # Sort words (position number is now at the front)
        words.sort()
        
        # Store final sentence words
        result = []  
        
        for word in words:
            # Remove number and reverse word
            ans = word[1:][::-1]  
            result.append(ans)
        
        # Join words into a sentence
        return " ".join(result)
