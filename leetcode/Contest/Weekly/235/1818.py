# 1818. Minimum Absolute Sum Difference
# https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        M = 10 ** 9 + 7        
        initial = 0
        max_diff = float('-inf')
        max_diff_i = 0
        
        for i, (a,b) in enumerate(zip(nums1, nums2)):
            diff = abs(a-b)
            if diff > max_diff:
                max_diff = diff
                max_diff_i = i
            initial += diff
        
        if initial == 0: return 0
        
        min_diff = float('inf')
        min_diff_i = 0
        a,b = nums1[max_diff_i], nums2[max_diff_i]
        
        for i,x in enumerate(nums1):
            diff = abs(x - b)
            if diff <= max_diff:
                min_diff = min(min_diff, diff)
                min_diff_i = i
        
        initial -= max_diff - min_diff
​
        return initial % M
