# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([x, 1])
        
        return "".join(ch * x for ch,x in stack)
        
