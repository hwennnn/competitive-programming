# 2309. Greatest English Letter in Upper and Lower Case
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        
        for j in range(25, -1, -1):
            if chr(ord("a") + j) in s and chr(ord("A") + j) in s:
                return chr(ord("A") + j)
        
        return ""
