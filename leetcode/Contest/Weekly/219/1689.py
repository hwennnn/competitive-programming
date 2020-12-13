# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        res = float('-inf')
        
        for c in n:
            res = max(int(c), res)    
        
        return res