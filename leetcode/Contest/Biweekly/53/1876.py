# 1876. Substrings of Size Three with Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for i in range(n - 2):
            if len(set(s[i:i+3])) == 3:
                res += 1
        
        return res
