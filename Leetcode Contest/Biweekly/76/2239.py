# 2239. Find Closest Number to Zero
# https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = float('inf')
        
        for x in nums:
            if abs(x) < abs(m):
                m = x
            elif abs(x) == abs(m):
                m = max(m, x)
        
        return m
