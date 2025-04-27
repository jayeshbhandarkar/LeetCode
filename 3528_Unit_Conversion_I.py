class Solution(object):
    def baseUnitConversions(self, conversions):
        n = len(conversions) + 1
        mod = 10**9 + 7
        graph = defaultdict(list)

        for u, v, factor in conversions:
            graph[u].append((v, factor))

        ans = [0] * n
        ans[0] = 1

        queue = deque()
        queue.append(0)

        while queue:
            curr = queue.popleft()
            for neighbor, factor in graph[curr]:
                ans[neighbor] = (ans[curr] * factor) % mod
                queue.append(neighbor)

        return ans
