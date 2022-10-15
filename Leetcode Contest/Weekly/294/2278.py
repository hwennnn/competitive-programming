# 2278. Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        c = s.count(letter)
​
        return int(c / n * 100)
