# 1781. Sum of Beauty of All Substrings
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for i in range(n):
            mp = collections.defaultdict(int)
            for j in range(i, n):
                mp[s[j]] += 1
                v = mp.values()
                res += max(v) - min(v)
        
        return res
