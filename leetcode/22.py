# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        
        def backtrack(s, left, right):
            if len(s) == n*2:
                res.append(s)
                return
            
            if left < n:
                backtrack(s+"(", left+1, right)
                
            if right < left:
                backtrack(s+")", left, right+1)
            

        backtrack("", 0, 0)
        
        return res