# 1911. Maximum Alternating Subsequence Sum
# https://leetcode.com/problems/maximum-alternating-subsequence-sum

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def go(isPos, i):
            if i >= len(nums): return 0
            
            curr = nums[i] if isPos else -nums[i]
            
            return max(curr + go(not isPos, i + 1), go(isPos, i + 1))
        
        return go(True, 0)
