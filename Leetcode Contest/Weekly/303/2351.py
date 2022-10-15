# 2351. First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        
        for x in s:
            if x in seen:
                return x
            
            seen.add(x)
