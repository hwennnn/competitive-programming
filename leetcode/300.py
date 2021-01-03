# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]):
        stack = []
        for x in nums:
            index = bisect_left(stack, x)
            if index == len(stack):
                stack.append(x)
            else:
                stack[index] = x
        
        return len(stack)
    
    def lengthOfLIS(self, nums: List[int]):
        res = 1
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            
            res = max(res, dp[i])
        
        return res