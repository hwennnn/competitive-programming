# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        k = 0
        
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                k += 1
            
            if k > 1: return False
                
        return True
            
            
