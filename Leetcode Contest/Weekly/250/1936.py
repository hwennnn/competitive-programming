# 1936. Add Minimum Number of Rungs
# https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = res = 0
        
        for rung in rungs:
            res += (rung - prev - 1) // dist
            prev = rung
        
        return res
