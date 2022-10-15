# 1706. Where Will the Ball Fall
# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        
        for c in range(len(grid[0])):
            res.append(self.helper(grid, 0, c))
        
        return res
    
    def helper(self, grid, r, c):
        if r == len(grid): return c
        
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]):
            
            if c == 0 and grid[r][c] == -1: return -1
            
            elif c == len(grid[r]) - 1 and grid[r][c] == 1: return -1
            
            elif c < len(grid[r]) - 1 and grid[r][c] == 1 and grid[r][c+1] == -1: return -1
            
            elif c > 0 and grid[r][c-1] == 1 and grid[r][c] == -1: return -1
            
            return self.helper(grid, r+1, c + grid[r][c])
        
        return -1