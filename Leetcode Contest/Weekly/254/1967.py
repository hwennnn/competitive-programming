# 1967. Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        
        for p in patterns:
            if p in word:
                res += 1
        
        return res
