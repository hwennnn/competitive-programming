# 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res, i, j = 0, 0, n - 1
        
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        
        return res
        
