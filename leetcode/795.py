# 795. Number of Subarrays with Bounded Maximum
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = dp = 0
        prev = -1
        
        for i, x in enumerate(nums):
            if x < left and i > 0:
                res += dp
            
            if x > right:
                prev = i
                dp = 0
            
            if left <= x <= right:
                dp = i - prev
                res += dp
        
        return res
