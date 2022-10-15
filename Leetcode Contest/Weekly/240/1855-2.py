# 1855. Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    
        n1, n2 = len(nums1), len(nums2)
        res = 0
        i = j = 0
        
        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        
        return res
