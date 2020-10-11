# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, S: str) -> int:
        depth = 0
        res = 0
        
        for s in S:
            if s == "(":
                depth += 1
            elif s == ")":
                depth -= 1

            res = max(res, depth)
        
        return res