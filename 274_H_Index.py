class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        sort_citations = sorted(citations, reverse = True)
        h = 0

        for i in range(0, n):
            if sort_citations[i] >= i+1:
                h += 1

        return h
        
