# 1685. Sum of Absolute Differences in a Sorted Array
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        left, right = 0, sum(nums)
        
        for i,x in enumerate(nums):
            right -= x
            
            l = (x * i) - left
            r = (right - (x*(n-i-1)))
            
            res[i] = l + r
            
            left += x
        
        return res
        