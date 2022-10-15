# 1654. Minimum Jumps to Reach Home
# https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        seen = set()
        f = set(forbidden)
        max_val = max([x]+forbidden) + a + b
        deq = collections.deque([(0,0,0)]) # now, count, isBackward
        
        while deq:
            now, count, isBackward = deq.popleft()
            
            if now == x:
                return count
            
            if now + a not in f and now + a <= max_val and (now+a, False) not in seen:
                deq.append((now+a, count+1, False))
                seen.add((now+a, False))
            
            if now - b not in f and now - b >= 0 and not isBackward and (now-b, isBackward) not in seen:
                deq.append((now-b, count+1, True))
                seen.add((now-b, True))
        
        return -1