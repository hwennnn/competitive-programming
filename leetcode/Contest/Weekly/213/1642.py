# 1642. Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)    
        m = float("inf")
        res = 0
        
        for i in range(n-1):
            if heights[i] >= heights[i+1]:
                res += 1
            else:
                d = heights[i+1] - heights[i]
                optimald = d
                if d > m:
                    optimald = m
                    m = d

                if bricks >= optimald:
                    res += 1
                    bricks -= optimald
                else:
                    if ladders > 0:
                        ladders -= 1
                        res += 1
                        m = d
                    else:
                        break
        
        return res
    
            