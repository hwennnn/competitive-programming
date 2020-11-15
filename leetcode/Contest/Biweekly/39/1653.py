# 1653. Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        c = collections.Counter(s)
        
        a_left = b_left = 0
        a_right, b_right = c["a"], c["b"]
        
        res = len(s)
        
        for x in s:
            res = min(res, a_right + b_left)
            if x == "a":
                a_left += 1
                a_right -= 1
            else:
                b_left += 1
                b_right -= 1
        
        
        res = min(res, a_right + b_left)
        
        return res
