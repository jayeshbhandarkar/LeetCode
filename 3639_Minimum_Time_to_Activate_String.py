from bisect import bisect_left, insort

class Solution(object):
    def minTime(self, s, order, k):
        n = len(s)
        total = n * (n + 1) // 2
        stars = [] 
        invalid = total

        def sum_len(x):
            return x * (x + 1) // 2

        for t in range(n):
            idx = order[t]
            insort(stars, idx)

            i = bisect_left(stars, idx)
            l = stars[i - 1] if i > 0 else -1
            r = stars[i + 1] if i + 1 < len(stars) else n

            seg_len = r - l - 1
            invalid -= sum_len(seg_len)

            if idx - l - 1 > 0:
                invalid += sum_len(idx - l - 1)
            if r - idx - 1 > 0:
                invalid += sum_len(r - idx - 1)

            valid = total - invalid
            if valid >= k:
                return t

        return -1
