class Solution(object):
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        visited = set()

        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        def dfs(r, c):
            stack = [(r, c)]
            total = 0
            while stack:
                x, y = stack.pop()
                if (x, y) in visited or grid[x][y] == 0:
                    continue
                visited.add((x, y))
                total += grid[x][y]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] > 0:
                        stack.append((nx, ny))
            return total

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in visited:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        count += 1

        return count
