# 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        median = nums[n // 2] if n % 2 else (nums[n // 2] + nums[n // 2 - 1]) // 2
        
        return sum(abs(x - median) for x in nums)
