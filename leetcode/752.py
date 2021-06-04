# 752. Open the Lock
# https://leetcode.com/problems/open-the-lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forbidden = set(deadends)
        visited = set(['0000'])
        queue = collections.deque([('0000', 0)])
        
        def construct(lock):
            res = []
            
            for i in range(4):
                if lock[i] == '0':
                    res.append(lock[:i] + '9' + lock[i + 1:])
                    
                res.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:])
                res.append(lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i + 1:])
​
            return res
        
        while queue:
            current, step = queue.popleft()
            
            if current not in forbidden:
                if current == target: return step
​
                for p in construct(current):
                    if p not in visited and p not in forbidden:
                        queue.append((p, step + 1))
                        visited.add(p)
        
        return -1
