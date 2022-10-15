# 2397. Maximum Rows Covered by Columns
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution:
    def maximumRows(self, mat: List[List[int]], k: int) -> int:
        rows, cols = len(mat), len(mat[0])
        res = 0
        
        A = list(range(cols))
​
        for comb in combinations(A, k):
            filled = 0
            
            for row in mat:
                ones = row.count(1)
                curr = 0
                
                for index in comb:
                    if row[index] == 1:
                        curr += 1
                
                if curr == ones:
                    filled += 1
                
            res = max(res, filled)
            
        return res
