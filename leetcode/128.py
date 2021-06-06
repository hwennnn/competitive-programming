# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        
        for x in nums:
            if x - 1 not in s:
                y = x + 1
                
                while y in s:
                    y += 1
                
                res = max(res, y - x)
        
        return res
