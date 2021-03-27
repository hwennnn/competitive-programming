# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for mid in range(n):
            
            left = right = mid
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            
            if mid + 1 < n:
                left = mid
                right = mid + 1
                while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                    res += 1
        
        return res
