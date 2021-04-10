# 1781. Sum of Beauty of All Substrings
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            for j in range(i+1, n):
                sub = s[i:j+1]
                c = collections.Counter(sub)
                if len(c) > 1:
                    res += max(c.values()) - min(c.values())
        
        return res
