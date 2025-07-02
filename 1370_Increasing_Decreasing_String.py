from collections import Counter

class Solution(object):
    def sortString(self, s):
        res = []
        d = Counter(s)
        keys = sorted(d.keys())
        total = len(s)

        while total > 0:
            for k in keys + keys[::-1]:
                if d[k] > 0:
                    res.append(k)
                    d[k] -= 1
                    total -= 1

        return "".join(res)
