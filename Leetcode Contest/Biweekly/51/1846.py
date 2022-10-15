# 1846. Maximum Element After Decreasing and Rearranging
# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        
        arr[0] = 1
        for i in range(1, n):
            arr[i] = min(arr[i - 1] + 1, arr[i])
        
        return max(arr)
