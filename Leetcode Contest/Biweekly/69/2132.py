# 2132. Stamping the Grid
# https://leetcode.com/problems/stamping-the-grid/

class Solution:
    def possibleToStamp(self, grid: List[List[int]], H: int, W: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
​
        for x in range(rows):
            for y in range(cols):
                prefix[x + 1][y + 1] = prefix[x + 1][y] + prefix[x][y + 1] - prefix[x][y] + grid[x][y]
​
        diff = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for x in range(rows - H + 1):
            for y in range(cols - W + 1):
                rect = prefix[x + H][y + W] - prefix[x + H][y] - prefix[x][y + W] + prefix[x][y]
​
                if rect == 0:
                    diff[x][y] += 1
                    diff[x + H][y] -= 1
                    diff[x][y + W] -= 1
                    diff[x + H][y + W] += 1
​
        for x in range(rows + 1):
            for y in range(cols):
                diff[x][y + 1] += diff[x][y]
        
        for y in range(cols + 1):
            for x in range(rows):
                diff[x + 1][y] += diff[x][y]
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0 and diff[x][y] == 0:
                    return False
        
        return True
                    
​
