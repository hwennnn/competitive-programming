# 673. Number of Longest Increasing Subsequence
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n
        count = [1] * n
        m = 1
        
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            
            m = max(m, dp[i])
        
        res = 0
        for i in range(n):
            if dp[i] == m:
                res += count[i]

        return res