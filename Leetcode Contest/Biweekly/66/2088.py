# 2088. Count Fertile Pyramids in a Land
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        reverseGrid = [row[:] for row in grid][::-1]
        
        def count(grid):
            res = 0
            
            for i in range(1, rows):
                for j in range(1, cols - 1):
                    if grid[i][j] and grid[i - 1][j]:
                        grid[i][j] = 1 + min(grid[i - 1][j - 1], grid[i - 1][j + 1])
                        res += grid[i][j] - 1
            
            return res
        
        return count(grid) + count(reverseGrid)
