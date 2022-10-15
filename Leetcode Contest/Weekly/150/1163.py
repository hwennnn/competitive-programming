# 1163. Last Substring in Lexicographical Order
# https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution:
    def lastSubstring(self, s: str) -> str:
        biggest = max(s)
        res = ""
        
        for i,c in enumerate(s):
            if c == biggest:
                res = max(res, s[i:])
        
        return res
        
