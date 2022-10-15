# 1981. Minimize the Difference Between Target and Chosen Elements
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        nums = {0}
        
        for row in mat:
            nums = {num + x for x in row for num in nums}
        
        return min(abs(x - target) for x in nums)
