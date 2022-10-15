# 2002. Maximum Product of the Length of Two Palindromic Subsequences
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        N = 1 << n
        dp = [0] * N
        res = 0
        
        def palSize(mask):
            i, j, count = 0, n - 1, 0
            
            while i <= j:
                if (mask & (1 << i)) == 0:
                    i += 1
                elif (mask & (1 << j)) == 0:
                    j -= 1
                elif s[i] != s[j]:
                    return 0
                else:
                    if i == j:
                        count += 1
                    else:
                        count += 2
                    
                    i += 1
                    j -= 1
            
            return count
        
        for mask in range(1, N):
            dp[mask] = palSize(mask)
​
        for m1 in range(1, N):
            if dp[m1]:
                for m2 in range(1, N):
                    if m1 & m2 == 0:
                        res = max(res, dp[m1] * dp[m2])
        
        return res
        
