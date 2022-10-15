# 2172. Maximum AND Sum of Array
# https://leetcode.com/problems/maximum-and-sum-of-array

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        fullMask = (1 << n) - 1
        
        @cache
        def go(index, mask1, mask2):
            if index == n: return 0
            
            res = 0
            
                
            for slot in range(numSlots):
                y = nums[index] & (slot + 1)
​
                if mask1 & (1 << slot) == 0:
                    res = max(res, y + go(index + 1, mask1 ^ (1 << slot), mask2))
                elif mask2 & (1 << slot) == 0:
                    res = max(res, y + go(index + 1, mask1, mask2 ^ (1 << slot)))
            
            return res
        
        return go(0, 0, 0)
