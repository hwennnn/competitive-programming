# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        res = 1
        seen = set()
        
        for j, x in enumerate(s):
            if x in seen:
                seen.clear()
                res += 1
                
            seen.add(x)
        
        return res
