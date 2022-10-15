# 2078. Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    res = max(res, abs(j - i))
        
        return res
