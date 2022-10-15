# 2193. Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        n = len(s)
        res = 0
        start, end = 0, n - 1
        
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                i = end - 1
                
                while i > start and s[i] != s[start]:
                    i -= 1
                
                if i == start:
                    s[i], s[i + 1] = s[i + 1], s[i]
                    res += 1
                else:
                    while i < end:
                        s[i], s[i + 1] = s[i + 1], s[i]
                        i += 1
                        res += 1
                    start += 1
                    end -= 1
        
        return res
