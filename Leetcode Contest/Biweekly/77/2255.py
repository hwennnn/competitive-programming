# 2255. Count Prefixes of a Given String
# https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        
        for x in words:
            if s.startswith(x):
                res += 1
        
        return res
