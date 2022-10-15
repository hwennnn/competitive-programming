# 2148. Count Elements With Strictly Smaller and Greater Elements 
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            smaller = False
            
            for j in range(i):
                if nums[j] < nums[i]:
                    smaller = True
                    break
            
            larger = False
            
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    larger = True
                    break
            
            res += int(larger and smaller)
        
        
        return res
