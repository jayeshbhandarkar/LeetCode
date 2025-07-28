class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)

            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
        
