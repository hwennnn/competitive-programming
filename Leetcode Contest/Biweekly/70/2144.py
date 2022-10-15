# 2144. Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = 1)
        n = len(cost)
        res = i = 0
        
        while i + 2 < n:
            res += cost[i] + cost[i + 1]
            i += 3
        
        return res + sum(cost[i:])
