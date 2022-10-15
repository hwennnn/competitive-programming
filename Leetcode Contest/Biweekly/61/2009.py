# 2009. Minimum Number of Operations to Make Array Continuous
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        nums = sorted(set(nums))
        
        for i, start in enumerate(nums):
            end = start + n - 1
            index = bisect.bisect_right(nums, end)
            between = index - i
            res = min(res, n - between)
        
        return res
​
