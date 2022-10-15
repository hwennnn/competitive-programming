# 1911. Maximum Alternating Subsequence Sum
# https://leetcode.com/problems/maximum-alternating-subsequence-sum

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = even = 0
        
        for x in nums:
            even = max(even, odd + x)
            odd = even - x
        
        return even
