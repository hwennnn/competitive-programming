# 1147. Longest Chunked Palindrome Decomposition
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        res, l, r = 0, "", ""
        
        for a,b in zip(text, text[::-1]):
            l, r = l + a, b + r
            
            if l == r:
                res, l, r = res + 1, "", ""
        
        return res
