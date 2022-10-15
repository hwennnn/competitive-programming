# 2124. Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        aCount = 0
        a = s.count("a")
        
        for c in s:
            if c == "a":
                aCount += 1
            elif c == "b":
                if aCount != a:
                    return False
        
        return True
