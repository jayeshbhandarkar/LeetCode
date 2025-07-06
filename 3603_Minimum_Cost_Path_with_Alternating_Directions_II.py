import heapq

class Solution(object):
    def minCost(self, m, n, waitCost):
        heap = []
        
        start_cost = (0 + 1) * (0 + 1)
        heapq.heappush(heap, (start_cost, 0, 0, 1))

        visited = {}

        while heap:
            cost, i, j, t = heapq.heappop(heap)

            if (i, j) == (m - 1, n - 1):
                return cost

            key = (i, j, t % 2)
            if key in visited and visited[key] <= cost:
                continue
            visited[key] = cost

            if t % 2 == 1:
                if i + 1 < m:
                    ni, nj = i + 1, j
                    entry_cost = (ni + 1) * (nj + 1)
                    heapq.heappush(heap, (cost + entry_cost, ni, nj, t + 1))
                    
                if j + 1 < n:
                    ni, nj = i, j + 1
                    entry_cost = (ni + 1) * (nj + 1)
                    heapq.heappush(heap, (cost + entry_cost, ni, nj, t + 1))
                    
            else:
                wait = waitCost[i][j]
                heapq.heappush(heap, (cost + wait, i, j, t + 1))
