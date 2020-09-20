# 1593. Split a String Into the Max Number of Unique Substrings
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, S: str) -> int:
        def backtrack(S, seen):
            res = 0
            for i in range(1,len(S)+1):
                s = S[:i]
                if s not in seen:
                    seen.add(s)
                    res = max(res, 1 + backtrack(S[i:], seen))
                    seen.remove(s)
            
            return res
        
        seen = set()
        return backtrack(S, seen)
    
        
                
        