# 2216. Minimum Deletions to Make Array Beautiful
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        prev = None
        valid = 0
        
        for x in nums:
            if prev is not None:
                if x != prev:
                    prev = None
                    valid += 2
            else:
                prev = x
        
        return n - valid
