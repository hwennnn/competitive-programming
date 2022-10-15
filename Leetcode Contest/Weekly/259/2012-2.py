# 2012. Sum of Beauty in the Array
# https://leetcode.com/problems/sum-of-beauty-in-the-array

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left = nums[0]
        right = [0] * n
        right[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        
        res = 0
        
        for i in range(1, n - 1):
            if left < nums[i] < right[i + 1]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
                
            left = max(left, nums[i])
        
        return res
            
