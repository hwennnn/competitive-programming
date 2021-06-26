# 1911. Maximum Alternating Subsequence Sum
# https://leetcode.com/problems/maximum-alternating-subsequence-sum

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        odd = [0] * n
        even = [0] * n
        
        odd[0] = nums[0]
        
        for i in range(1, n):
            odd[i] = max(odd[i - 1], even[i - 1] + nums[i])
            even[i] = max(even[i - 1], odd[i - 1] - nums[i])
​
        return odd[-1]
