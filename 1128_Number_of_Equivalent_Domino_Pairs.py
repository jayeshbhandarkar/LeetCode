class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        freq = {}
        count = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            
            if key in freq:
                count += freq[key]
                freq[key] += 1

            else:
                freq[key] = 1
                
        return count
        
