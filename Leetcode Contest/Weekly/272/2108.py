# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        
        for x in words:
            if x == x[::-1]:
                return x
        
        return res
