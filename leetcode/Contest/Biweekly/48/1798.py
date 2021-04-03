# 1798. Maximum Number of Consecutive Values You Can Make
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 1
        
        for v in sorted(coins):
            if v > res:
                return res
            res += v
        
        return res
