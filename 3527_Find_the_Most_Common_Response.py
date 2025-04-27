from collections import defaultdict

class Solution(object):
    def findCommonResponse(self, responses):
        count = defaultdict(int)

        for day in responses:
            unique_responses = set(day)
            for response in unique_responses:
                count[response] += 1

        max_freq = max(count.values())

        most_common = []
        for response, freq in count.items():
            if freq == max_freq:
                most_common.append(response)

        result = min(most_common)
        return result
        
