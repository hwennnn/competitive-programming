# 667. Beautiful Arrangement II
# https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        l, r = 1, k + 1
        i = 0
        
        while i < k:
            res.append(l)
            l += 1
            i += 1
            
            res.append(r)
            r -= 1
            i += 1
            
        if l == r: 
            res.append(r)
            i += 1
        
        while i < n:
            res.append(i + 1)
            i += 1
        
        return res
