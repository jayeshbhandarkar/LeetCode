from collections import defaultdict
import heapq

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        edge_list = edges  

        graph = defaultdict(list)
        for u, v, cost in edge_list:
            graph[u].append((v, cost))

        def is_possible(min_edge):
            heap = [(0, 0)] 
            dist = [float('inf')] * n
            dist[0] = 0

            while heap:
                total, u = heapq.heappop(heap)
                if u == n - 1:
                    return True
                for v, cost in graph[u]:
                    if cost >= min_edge and online[v]:
                        new_total = total + cost
                        if new_total <= k and new_total < dist[v]:
                            dist[v] = new_total
                            heapq.heappush(heap, (new_total, v))
            return False

        costs = [c for _, _, c in edge_list]
        right = max(costs) if costs else 0
        left = 0
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                left = mid + 1 
            else:
                right = mid - 1

        return answer
