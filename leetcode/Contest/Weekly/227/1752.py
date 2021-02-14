# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        start = 0
        
        for i,x in enumerate(nums):
            if i == 0: continue
            
            if x >= nums[i-1]: continue
            else:
                if start != 0: return False
                start = i
                
        return sorted(nums) == nums[start:] + nums[:start]
            
            
