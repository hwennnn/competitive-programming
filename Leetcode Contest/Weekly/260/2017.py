# 2017. Grid Game
# https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        top, down = sum(grid[0]), 0
        res = float('inf')
        
        for i in range(cols):
            top -= grid[0][i]
            res = min(res, max(top, down))
            down += grid[1][i]
        
        return res
        
        
