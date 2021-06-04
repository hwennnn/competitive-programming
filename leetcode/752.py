# 752. Open the Lock
# https://leetcode.com/problems/open-the-lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forbidden = set(deadends)
        visited = set(['0000'])
        queue = collections.deque([('0000', 0)])
        
        while queue:
            lock, step = queue.popleft()
            
            if lock in forbidden: continue
            if lock == target: return step
            
            for i in range(4):
                w1 = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:]
                w2 = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i + 1:]
                
                for p in (w1, w2):
                    if p not in visited and p not in forbidden:
                        queue.append((p, step + 1))
                        visited.add(p)
​
        return -1
