# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        for x in nums:
            if x - 1 not in s:
                y = x + 1
                
                if y in s:
                    while y in s:
                        y += 1

                res = max(res, y - x)
        
        return res