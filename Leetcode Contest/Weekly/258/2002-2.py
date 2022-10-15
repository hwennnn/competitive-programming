# 2002. Maximum Product of the Length of Two Palindromic Subsequences
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        @cache
        def isPalindrome(word):
            i, j = 0, len(word) - 1
            
            while i < j and word[i] == word[j]:
                i += 1
                j -= 1
            
            return i >= j
        
        @cache
        def go(i, word1, word2):
            if i == n:
                if isPalindrome(word1) and isPalindrome(word2):
                    return len(word1) * len(word2)
                return 0
            
            s1 = go(i + 1, word1, word2)
            s2 = go(i + 1, word1 + s[i], word2)
            s3 = go(i + 1, word1, word2 + s[i])
            
            return max(s1, s2, s3)
        
        return go(0, '', '')
