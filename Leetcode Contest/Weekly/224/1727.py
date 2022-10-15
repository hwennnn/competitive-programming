# 1727. Largest Submatrix With Rearrangements
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution:
    def largestSubmatrix(self, A: List[List[int]]):
        rows, cols = len(A), len(A[0])

        for i in range(1,rows):
            for j in range(cols):
                if A[i][j] == 1:
                    A[i][j] += A[i-1][j]
        
        res = 0
        for i in range(rows):
            row = sorted(A[i])
            for j in range(cols):
                res = max(res, row[j] * (cols - j))
        
        return res
                
            