# 2290. Minimum Obstacle Removal to Reach Corner
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
​
        while queue:
            x, y = queue.popleft()
​
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited:
                    dp[dx][dy] = min(dp[dx][dy], dp[x][y] + grid[dx][dy])
                    visited.add((dx, dy))
                    if grid[dx][dy] == 1:
                        queue.append((dx, dy))
                    else:
                        queue.appendleft((dx, dy))
                            
        return dp[-1][-1]
