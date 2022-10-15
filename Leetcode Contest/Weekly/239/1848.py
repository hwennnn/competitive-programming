# 1848. Minimum Distance to the Target Element
# https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float('inf')
        
        for i,x in enumerate(nums):
            if x == target:
                res = min(res, abs(i - start))
        
        return res
