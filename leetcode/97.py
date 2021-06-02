# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        queue = collections.deque([(0, 0, 0)])
        visited = set()
        
        while queue:
            p1, p2, p3 = queue.popleft()
            if p1 == n1 and p2 == n2 and p3 == n3: return True
            
            if p3 < n3:
                if p1 < n1 and s1[p1] == s3[p3] and (p1 + 1, p2, p3 + 1) not in visited:
                    queue.append((p1 + 1, p2, p3 + 1))
                    visited.add((p1 + 1, p2, p3 + 1))
​
                if p2 < n2 and s2[p2] == s3[p3] and (p1, p2 + 1, p3 + 1) not in visited:
                    queue.append((p1, p2 + 1, p3 + 1))
                    visited.add((p1, p2 + 1, p3 + 1))
        
        return False
