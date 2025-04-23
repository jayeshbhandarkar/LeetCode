class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1

            else:
                count[i] = 1

        freq_values = count.values()
        return len(freq_values) == len(set(freq_values))
        
