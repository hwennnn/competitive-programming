# 1749. Maximum Absolute Sum of Any Subarray
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mmax = mmin = s = 0
        
        for num in nums:
            s += num
            mmax = max(mmax, s)
            mmin = min(mmin, s)
​
        return mmax - mmin
