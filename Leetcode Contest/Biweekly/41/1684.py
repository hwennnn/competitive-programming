# 1684. Count the Number of Consistent Strings
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        
        res = 0
        for w in words:
            c = set(w)
            found = True
            for i in c:
                if i not in s:
                    found = False
                    break
                    
            
            if found: res += 1
        
        return res