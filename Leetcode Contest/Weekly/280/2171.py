# 2171. Removing Minimum Number of Magic Beans
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        res = float('inf')
        n = len(beans)
        
        for i, x in enumerate(beans):
            res = min(res, total - (n - i) * x)
        
        return res
