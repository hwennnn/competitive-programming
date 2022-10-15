# 1974. Minimum Time to Type Word Using Special Typewriter
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        pos = 0
        
        for w in word:
            wpos = ord(w) - ord('a')
            res += min(abs(pos + 25 - wpos + 1), abs(wpos - pos), abs(wpos + 25 - pos + 1))
            pos = wpos
        
        return res
