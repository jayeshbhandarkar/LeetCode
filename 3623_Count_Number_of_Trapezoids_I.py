from collections import defaultdict

class Solution(object):
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        ym = defaultdict(list)

        for x, y in points:
            ym[y].append(x)

        seg_counts = []
        for y in ym:
            cnt = len(ym[y])
            if cnt >= 2:
                seg_counts.append((cnt * (cnt - 1)) // 2)

        total = sum(seg_counts)
        ans = 0
        for seg in seg_counts:
            total -= seg
            ans = (ans + seg * total) % MOD

        return ans
