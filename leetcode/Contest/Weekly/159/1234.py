# 1234. Replace the Substring for Balanced String
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        res = float('inf')
        i = 0
        
        for j,x in enumerate(s):
            c[x] -= 1
            
            while i < n and all(val <= n//4 for val in c.values()):
                res = min(res, j - i + 1)
                c[s[i]] += 1
                i += 1
        
        return res