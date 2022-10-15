# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        
        return res
