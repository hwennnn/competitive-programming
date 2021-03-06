# 1260. Shift 2D Grid
# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int):
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        return [nums[i:i+col] for i in range(0, len(nums), col)]

    def shiftGrid(self, grid: List[List[int]], k: int):
        rows, cols = len(grid), len(grid[0])
        
        for _ in range(k):
            res = [[0]*cols for _ in range(rows)]
            for i in range(rows):
                if i + 1 < rows and cols > 0:
                    res[i+1][0] = grid[i][cols-1]
                    
                for j in range(cols):
                    if j + 1 < cols:
                        res[i][j+1] = grid[i][j]

            if rows > 0 and cols > 0:
                res[0][0] = grid[rows-1][cols-1]
            
            grid = res
            
        return grid