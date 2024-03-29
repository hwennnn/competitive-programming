# 2027. Minimum Moves to Convert String
# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        n = len(s)
        res = i = 0
        
        while i < n:
            hasX = False
            if s[i] == 'X':
                for j in range(3):
                    if i + j < n and s[i + j] == 'X':
                        hasX = True
                        s[i + j] = 'O'
                if hasX:
                    res += 1
                i += 3
            else:
                i += 1
​
        return res
