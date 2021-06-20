# 1905. Count Sub Islands
# https://leetcode.com/problems/count-sub-islands

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        
        res = 0
        
        def dfs(x, y):
            grid2[x][y] = 0
            res = grid1[x][y]
            
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and grid2[dx][dy] == 1:
                    res &= dfs(dx, dy)
            
            return res
            
        
        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] == grid2[i][j] == 1:
                    res += dfs(i, j)
                    
        return res
