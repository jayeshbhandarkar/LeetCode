import heapq
from collections import defaultdict

class Solution(object):
    def minTime(self, n, edges):
        g = defaultdict(list)
        for u, v, s, e in edges:
            g[u].append((v, s, e))

        h = [(0, 0)]
        vis = [float('inf')] * n
        vis[0] = 0

        while h:
            t, u = heapq.heappop(h)
            if u == n - 1:
                return t
            if t > vis[u]:
                continue
            if t + 1 < vis[u]:
                vis[u] = t + 1
                heapq.heappush(h, (t + 1, u))
            for v, s, e in g[u]:
                nt = s if t < s else t
                if nt > e:
                    continue
                arr = nt + 1
                if arr < vis[v]:
                    vis[v] = arr
                    heapq.heappush(h, (arr, v))

        return -1
