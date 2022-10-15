# 1252. Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        grid = [[0]*m for _ in range(n)]
        
        for r,c in indices:
            for i in range(n):
                for j in range(m):
                    if j == c:
                        grid[i][j] += 1
                    if i == r: 
                        grid[i][j] += 1
        
        return sum(1 for num in sum(grid,[]) if num & 1)
                    
        