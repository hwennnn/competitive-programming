# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2

        def count(s):
            return sum(c in "aeiouAEIOU" for c in s)
        
        return count(s[:half]) == count(s[half:])
        
        