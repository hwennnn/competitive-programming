# 1139. Largest 1-Bordered Square
# https://leetcode.com/problems/largest-1-bordered-square/

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        
        def check(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def dfs(i, j, size):
            res = 1
            isValid = canContinue = True
            mx, my = i + size, j + size
            
            if not check(mx, my): return res
            
            for dy in range(j, my + 1):
                if check(i, dy) and check(mx, dy) and grid[i][dy] == 0 or grid[mx][dy] == 0:
                    isValid = False
                    if grid[i][dy] == 0: 
                        canContinue = False
            
            for dx in range(i, mx + 1):
                if check(dx, j) and check(dx, my) and grid[dx][j] == 0 or grid[dx][my] == 0:
                    isValid = False
                    if grid[dx][j] == 0:
                        canContinue = False
                    
            if isValid:
                res = max(res, (size + 1) * (size + 1))
​
            if canContinue and check(i + size + 1, j + size + 1):
                res = max(res, dfs(i, j, size + 1))
            
            return res 
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j, 0))
        
        return res
