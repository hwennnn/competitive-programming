# 1637. Widest Vertical Area Between Two Points Containing No Points
# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        points.sort(key = lambda x : (x[0], x[1]))
        
        res = 0
        prevX = points[0][0]
        for x,y in points[1:]:
            if x == prevX:
                continue
            else:
                res = max(res, x - prevX)
            prevX = x
        
        return res