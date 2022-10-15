# 2430. Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string

class Solution:
    def deleteString(self, s: str) -> int:
        N = len(s)
        if len(set(s)) == 1: return N
        
        dp = [1] * N
        
        for i in range(N - 1, -1, -1):
            for j in range(1, N):
                if i + 2 * j > N: break
                    
                if 1 + dp[i+j] > dp[i] and s[i:i+j] == s[i+j:i+2*j]:
                    dp[i] = 1 + dp[i+j]
​
        return dp[0]
