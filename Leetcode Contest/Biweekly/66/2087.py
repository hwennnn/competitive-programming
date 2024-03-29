# 2087. Minimum Cost Homecoming of a Robot in a Grid
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sx, sy = startPos
        ex, ey = homePos
        res = 0
        
        while sx < ex:
            sx += 1
            res += rowCosts[sx]
        
        while sx > ex:
            sx -= 1
            res += rowCosts[sx]
        
        while sy < ey:
            sy += 1
            res += colCosts[sy]
        
        while sy > ey:
            sy -= 1
            res += colCosts[sy]
        
        return res
