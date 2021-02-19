# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str):
        res = ""
        stack = []
        mp = {}
        
        for i,c in enumerate(s):
            if c == ")" and stack and stack[-1][1] == "(":
                x, p = stack.pop()
                mp[x] = p
                mp[i] = c
                
            elif c == "(":
                stack.append((i,c))
        
        
        for i,c in enumerate(s):
            if c == "(" or c == ")":
                if i in mp:
                    res += mp[i]
            else:
                res += c
        
        return res
​
        
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
​
        for i,c in enumerate(s):
            if c == ")":
                if stack: 
                    stack.pop()
                else:
                    s[i] = ""
​
            elif c == "(":
                stack.append(i)
​
​
        while stack:
            s[stack.pop()] = ""
​
        return "".join(s)
