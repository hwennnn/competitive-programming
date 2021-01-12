# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]):
        n = len(height)
        i, j = 0, n - 1
        res = 0
        
        while i < j:
            res = max(res, min(height[i], height[j]) * (j-i))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return res
            