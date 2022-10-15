# 2114. Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        
        for s in sentences:
            res = max(res, len(s.split()))
        
        return res
