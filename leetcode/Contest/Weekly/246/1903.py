# 1903. Largest Odd Number in String
# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, nums: str) -> str:
        res = None
        
        for i,x in enumerate(nums):
            if int(x) & 1:
                res = nums[:i + 1]
        
        return "" if not res else res
