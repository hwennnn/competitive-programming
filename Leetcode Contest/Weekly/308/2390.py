# 2390. Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for x in s:
            if x == "*":
                stack.pop()
            else:
                stack.append(x)
        
        return "".join(stack)
