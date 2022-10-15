# 1072. Flip Columns For Maximum Number of Equal Rows
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mp = collections.defaultdict(int)
        
        for r in matrix:
            A = []
            for c in r:
                A.append(r[0] ^ c)
            
            mp[tuple(A)] += 1
        
        return max(mp.values())
