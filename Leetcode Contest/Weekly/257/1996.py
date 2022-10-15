# 1996. The Number of Weak Characters in the Game
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game

class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:(x[0], -x[1]))
        stack = []
        res = 0
        
        for a,b in A:
            while stack and a > stack[-1][0] and b > stack[-1][1]:
                stack.pop()
                res += 1
            
            stack.append((a, b))
        
        return res
