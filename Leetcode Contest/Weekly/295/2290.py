# 2290. Minimum Obstacle Removal to Reach Corner
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
​
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        
        heap = [(0, 0, 0)]
        
        while heap:
            k, x, y = heappop(heap)
            
            if dist[x][y] != k:
                continue
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    old = dist[dx][dy]
                    new = k + grid[dx][dy]
                    
                    if new < old:
                        dist[dx][dy] = new
                        heappush(heap, (new, dx, dy))
                        
        return dist[-1][-1]
