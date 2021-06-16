# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        
        def backtrack(curr = [], opened = 0, closed = 0):
            if opened + closed == n * 2:
                res.add("".join(curr))
                return
            
            if closed < opened:
                curr.append(")")
                backtrack(curr, opened, closed + 1)
                curr.pop()
            
            if opened < n:
                curr.append("(")
                backtrack(curr, opened + 1, closed)
                curr.pop()
​
        
        backtrack()
        
        return list(res)
