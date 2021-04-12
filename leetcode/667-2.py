# 667. Beautiful Arrangement II
# https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        
        i, j = 1, n
        
        while i <= j:
            if k > 1:
                if k % 2 == 0:
                    res.append(j)
                    j -= 1
                else:
                    res.append(i)
                    i += 1
                k -= 1
            else:
                res.append(i)
                i += 1
        
        return res
