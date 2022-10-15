# 2321. Maximum Score Of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        def kadane(nums):
            curr = res = 0
            
            for x in nums:
                curr = max(x, curr + x)
                res = max(res, curr)
            
            return res
        
        def g(A, B):
            return sum(A) + kadane([b - a for a, b in zip(A, B)])
        
        return max(g(nums1, nums2), g(nums2, nums1))
