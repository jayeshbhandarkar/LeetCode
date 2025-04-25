class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        answer = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        result = []

        for i in range(k):
            result.append(answer[i][0])
        
        return result
