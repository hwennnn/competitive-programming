# 1796. Second Largest Digit in a String
# https://leetcode.com/problems/second-largest-digit-in-a-string

class Solution:
    def secondHighest(self, s: str) -> int:
        res = set(list(c for c in s if c.isdigit()))
    
        return sorted(list(res))[-2] if len(res) > 1 else -1
