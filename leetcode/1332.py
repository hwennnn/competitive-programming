# 1332. Remove Palindromic Subsequences
# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        return 2 - (s == s[::-1]) - (s == "")
