# 1866. Number of Ways to Rearrange Sticks With K Sticks Visible
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible

class Solution:
    @functools.lru_cache(None)
    def rearrangeSticks(self, n, k, M = 10**9 + 7):
        if n == k: return 1
        if k == 0: return 0
        return (self.rearrangeSticks(n - 1, k - 1) + self.rearrangeSticks(n - 1, k) * (n - 1)) % M
        
