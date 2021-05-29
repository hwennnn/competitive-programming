# 1877. Minimize Maximum Pair Sum in Array
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n // 2):
            res.append(nums[i] + nums[n - i - 1])
        
        return max(res)
