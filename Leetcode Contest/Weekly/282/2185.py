# 2185. Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        
        for word in words:
            if word.startswith(pref):
                res += 1
            
        return res
