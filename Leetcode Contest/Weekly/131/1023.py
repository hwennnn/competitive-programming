# 1023. Camelcase Matching
# https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = [False] * len(queries)
        n = len(pattern)
        
        for i, words in enumerate(queries):
            index = 0
            valid = True
            
            for word in words:
                if ord('A') <= ord(word) <= ord('Z') and (index == n or word != pattern[index]):
                    valid = False
                    
                if index < n and word == pattern[index]:
                    index += 1
            
            res[i] = valid and index == n
        
        return res
