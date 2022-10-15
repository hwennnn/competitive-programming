# 1631. Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        def isPath(effort):
            seen, deq = {(0,0)}, deque([(0,0)])
            
            while deq:
                x,y = deq.popleft()
                if x == R-1 and y == C-1:
                    return True
                for r,c in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
                    if R > r >= 0 <= c < C and abs(A[r][c] - A[x][y]) <= effort and (r,c) not in seen:
                        seen.add((r,c))
                        deq.append((r,c))
            
            return False
        
        low, high = 0, 10**6
        
        while low < high:
            effort = low + high >> 1
            if not isPath(effort):
                low = effort + 1
            else:
                high = effort
        
        return low 