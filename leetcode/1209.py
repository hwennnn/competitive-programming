# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                ch, count = stack.pop()
                stack.append((ch, count + 1))
            else:
                stack.append((x, 1))
            
            if stack and stack[-1][1] == k:
                stack.pop()
            
            while len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                ch, count = stack.pop()
                count += stack.pop()[1]
                stack.append((ch, count))
        
        res = ""
        
        for ch,count in stack:
            res += ch * count
        
        return res
        
