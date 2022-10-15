# 1871. Jump Game VII
# https://leetcode.com/problems/jump-game-vii

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        visited, mx = set([0]), 0
        queue = collections.deque([0])
        
        while queue:
            i = queue.popleft()
            
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, n)):
                if s[j] == "0" and j not in visited:
                    if j == n - 1: return True
                    queue.append(j)
                    visited.add(j)
            
            mx = max(mx, i + maxJump)
        
        return False
