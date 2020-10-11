# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        visited = set() # for constant lookup time
        stack = []
        
        for c in s:
            counter[c] -= 1
            if c in visited: continue
                
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                visited.remove(stack.pop())
            
            visited.add(c)
            stack.append(c)
        
        return "".join(stack)