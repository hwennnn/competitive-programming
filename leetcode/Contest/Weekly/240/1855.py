# 1855. Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    
        n1, n2 = len(nums1), len(nums2)
        res = 0
        i = j = 0
        
        while i < n1 or j < n2:
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                if j < n2 - 1:
                    j += 1
                elif i < n1 - 1:
                    i += 1
                else:
                    break
            else:
                if i < n1 - 1:
                    i += 1
                elif j < n2 - 1:
                    j += 1
                else:
                    break
        
        return res
