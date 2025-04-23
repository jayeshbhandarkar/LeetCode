from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)

        sorted_words = sorted(count.keys(), key=lambda word: (-count[word], word))

        return sorted_words[:k]
        
