# 2341. Maximum Number of Pairs in Array
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        removed = 0
        
        for x in Counter(nums).values():
            removed += x // 2
        
        return [removed, n - removed * 2]
