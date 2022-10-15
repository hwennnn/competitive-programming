# 1833. Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        res = 0
        costs.sort()
        
        for c in costs:
            if coins >= c:
                res += 1
                coins -= c
            else:
                break
        
        return res
