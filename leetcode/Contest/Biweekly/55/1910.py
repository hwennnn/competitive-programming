# 1910. Remove All Occurrences of a Substring
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        pn = len(part)
        
        for c in s:
            stack.append(c)
            
            if len(stack) >= pn and "".join(stack[-pn:]) == part:
                for _ in range(pn):
                    stack.pop()
​
        return "".join(stack)
