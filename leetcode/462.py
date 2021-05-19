# 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        return sum(abs(x - nums[len(nums) // 2]) for x in nums)
