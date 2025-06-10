class Solution(object):
    def maxDifference(self, s):
        count = Counter(s)
        even = []
        odd = []

        for i in count.values():
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        return max(odd) - min(even)      
        
