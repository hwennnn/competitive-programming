# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str):
        stack = []
        s = list(s)
        
        for i,c in enumerate(s):
            if c == ")":
                if stack: 
                    stack.pop()
                else:
                    s[i] = ""

            elif c == "(":
                stack.append(i)
            

        while stack:
            s[stack.pop()] = ""

        return "".join(s)
        
    def minRemoveToMakeValid(self, s: str):
        stack = []
        res = [""] * len(s)
        forbidden = set()
        
        for i,c in enumerate(s):
            if c == ")":
                if stack and stack[-1][1] == "(": 
                    stack.pop()
                    res[i] = c
                else:
                    forbidden.add(i)

            elif c == "(":
                res[i] = c
                stack.append((i,c))
            
            else:
                res[i] = c

        if len(stack) > 0:
            forbidden |= set([i for i,_ in stack])

            for i in forbidden:
                res[i] = ""

        return "".join(res)
        
    def minRemoveToMakeValid(self, s: str):
        stack = []
        res = []
        forbidden = set()
        
        for i,c in enumerate(s):
            if c != "(" and c != ")": 
                res.append(c)
            else:
                if c == ")":
                    if stack and stack[-1][1] == "(": 
                        stack.pop()
                        res.append(c)
                    else:
                        forbidden.add(i)
                    
                else:
                    res.append(c)
                    stack.append((i,c))

        if len(stack) > 0:
            forbidden |= set([i for i,_ in stack])
            ans = []
            for i,x in enumerate(s):
                if i not in forbidden:
                    ans.append(x)
            
            return "".join(ans)

        
        return "".join(res)