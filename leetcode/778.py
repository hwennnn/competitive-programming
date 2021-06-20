# 778. Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),  len(grid[0])
        
        def dfs(x, y, mmax, visited):
            if x == rows - 1 and y == cols - 1: return True
            
            visited.add((x, y))
​
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited and grid[dx][dy] <= mmax:
                    if dfs(dx, dy, mmax, visited): return True
                    if (x, y) in visited: visited.remove((x, y))
                        
            return False
            
        
        left, right = max(grid[0][0], grid[-1][-1]), 2500
        while left < right:
            mid = left + (right - left) // 2
​
            if dfs(0, 0, mid, set()):
                right = mid
            else:
                left = mid + 1
            
        return left
