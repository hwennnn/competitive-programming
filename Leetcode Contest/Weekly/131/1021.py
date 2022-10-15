# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        can = False
        count = 0
        res = []
        
        for x in s:
            if can:
                if x == '(':
                    res.append(x)
                    count += 1
                else:
                    res.append(x)
                    count -= 1
                
                if count == -1:
                    res.pop()
                    count = 0
                    can = False
                    
            if not can and x == '(':
                can = True
            
            
        
        return "".join(res)
