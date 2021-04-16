# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()
            
            while len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                _, count = stack.pop()
                stack[-1][1] += count
        
        return "".join(ch * x for ch,x in stack)
        
