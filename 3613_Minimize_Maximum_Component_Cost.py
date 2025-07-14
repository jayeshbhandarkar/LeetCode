class Solution(object):
    def __init__(self):
        self.parent = []
        self.num_components = 0

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_components -= 1
            return True
        return False

    def minCost(self, n, edges, k):
        def check(max_cost_limit):
            self.parent = list(range(n))
            self.num_components = n

            for u, v, w in edges:
                if w <= max_cost_limit:
                    self.union(u, v)
            
            return self.num_components <= k

        low = 0
        high = 0
        if edges:
            high = max(edge[2] for edge in edges)
        
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
