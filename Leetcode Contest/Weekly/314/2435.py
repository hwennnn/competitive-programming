# 2435. Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

M = 10 ** 9 + 7
​
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
​
        @cache
        def go(i, j, curr):
            if i == rows - 1 and j == cols - 1:
                return 1 if curr == 0 else 0
        
            count = 0
            
            for di, dj in [(i + 1, j), (i, j + 1)]:
                if 0 <= di < rows and 0 <= dj < cols:
                    count = (count + go(di, dj, (curr + grid[di][dj]) % k)) % M
​
            return count
        
        return go(0, 0, grid[0][0] % k)
