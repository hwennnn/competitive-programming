# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        
        for a,b in zip(heights, sorted(heights)):
            res += int(a != b)
        
        return res
