# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        for c in t:
            res += ord(c)
        
        for c in s:
            res -= ord(c)
            
        return chr(res)

    def findTheDifference2(self, s: str, t: str) -> str:
        res = 0
        
        for c in s+t:
            res ^= ord(c)
            
        return chr(res)